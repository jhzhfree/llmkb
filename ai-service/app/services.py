import re,os,httpx
from collections import defaultdict

def extract_knowledge(text):
    ps=[x.strip() for x in re.split(r'\n{2,}',text or '') if x.strip()]
    cards=[];claims=[]
    for p in ps[:20]:
        typ='PROCEDURE' if any(k in p for k in ['步骤','流程','如何','操作']) else ('RULE' if any(k in p for k in ['必须','禁止','应当']) else 'FACT')
        cards.append({'type':typ,'title':p.splitlines()[0][:80],'summary':p[:180],'content':p,'confidence':0.72})
        s=re.split(r'[。！？\n]',p)[0]
        if s: claims.append({'subject':s[:30],'predicate':'DESCRIBES','object':s[30:120] or s,'conditions':[],'confidence':0.65})
    return {'cards':cards,'claims':claims,'entities':[],'relations':[]}

def route(q):
    if any(k in q for k in ['错误码','配置项','接口']):return {'questionType':'EXACT','strategies':['bm25','vector']}
    if any(k in q for k in ['关系','依赖','关联','影响']):return {'questionType':'RELATION','strategies':['graph','vector','card']}
    if any(k in q for k in ['如何','步骤','流程','操作']):return {'questionType':'PROCEDURE','strategies':['card','bm25','vector']}
    if any(k in q for k in ['是否','支持','条件','规则']):return {'questionType':'CLAIM','strategies':['claim','card','graph']}
    return {'questionType':'FACT','strategies':['card','vector','bm25','claim']}

DATA=[
 {'id':'CARD001','title':'知识裁决','content':'候选知识发布前应执行重复检测、冲突检测、证据评分和裁决。'},
 {'id':'CLM001','title':'知识证据原则','content':'正式知识必须绑定可追溯证据，低置信度知识不得自动发布。'},
 {'id':'GRAPH001','title':'断言与证据关系','content':'断言通过 SUPPORTED_BY 关系关联证据，可用于可信性说明。'},
]

def recall(channel,q,topk):
    out=[]
    for i,x in enumerate(DATA):
        if channel=='claim' and not x['id'].startswith('CLM'):continue
        if channel=='graph' and not x['id'].startswith('GRAPH'):continue
        if channel=='card' and not x['id'].startswith('CARD'):continue
        out.append({**x,'channel':channel,'score':1/(i+1)})
    return out[:topk]

def rrf(sets,k=60,topk=10):
    scores=defaultdict(float);docs={}
    for items in sets.values():
        for rank,x in enumerate(items,1):scores[x['id']]+=1/(k+rank);docs[x['id']]=x
    return [{**docs[i],'score':s} for i,s in sorted(scores.items(),key=lambda x:x[1],reverse=True)[:topk]]

async def generate(prompt):
    provider=os.getenv('LLM_PROVIDER','mock')
    if provider=='ollama':
        url=os.getenv('LLM_BASE_URL','http://127.0.0.1:11434').rstrip('/')+'/api/generate'
        model=os.getenv('LLM_MODEL','qwen2.5:7b')
        async with httpx.AsyncClient(timeout=120) as c:
            r=await c.post(url,json={'model':model,'prompt':prompt,'stream':False});r.raise_for_status();return r.json().get('response',''),model
    return '基于已检索到的可信知识上下文生成回答。当前为 Mock 模型，可通过环境变量切换 Ollama。','mock'

async def query_engine(qid,kb,q,topk):
    rt=route(q);sets={s:recall(s,q,topk) for s in rt['strategies']};cand=rrf(sets,topk=topk)
    ctx='\n'.join([f"[证据{i+1}] {x['title']}\n{x['content']}" for i,x in enumerate(cand)])
    prompt=f'只能依据以下知识回答；证据不足时明确说明。\n问题：{q}\n{ctx}'
    answer,model=await generate(prompt)
    return {'queryId':qid,'rewrittenQueries':[q.strip()],'router':rt,'strategies':rt['strategies'],'candidates':cand,'context':ctx,'citations':[{'index':i+1,'id':x['id'],'title':x['title'],'channel':x['channel']} for i,x in enumerate(cand)],'answer':answer,'model':model}
