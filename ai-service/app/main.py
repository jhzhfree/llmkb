from fastapi import FastAPI
from app.routes import router
app=FastAPI(title="AI 原生企业知识库平台 - AI Service",version="1.0.0")
app.include_router(router)
@app.get('/health')
def health():return {'status':'UP'}
