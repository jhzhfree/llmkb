from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional,List,Dict,Any
from app.services import extract_knowledge,query_engine
router=APIRouter()
class ExtractReq(BaseModel):knowledgeBaseId:int;sourceId:Optional[int]=None;text:str=''
class QueryReq(BaseModel):queryId:Optional[str]=None;knowledgeBaseId:int;query:str;topK:int=10;userId:Optional[str]=None;permissionTags:Optional[List[str]]=None
@router.post('/ai/extract')
async def extract(r:ExtractReq):return extract_knowledge(r.text)
@router.post('/ai/query')
async def query(r:QueryReq):return await query_engine(r.queryId or '',r.knowledgeBaseId,r.query,r.topK)
@router.post('/ai/adjudicate')
async def adjudicate(p:Dict[str,Any]):return {'decision':'UNCERTAIN','requiresHumanReview':True,'reason':'默认保守裁决策略'}
@router.post('/ai/index')
async def index(p:Dict[str,Any]):return {'status':'ACCEPTED','message':'已预留异步索引 Provider'}
