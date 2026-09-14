# AI 原生企业知识库平台（llmkb）

`llmkb` 是一个面向企业知识生产、治理、检索和智能问答的 AI 原生知识库平台。

平台不是简单的“文档上传 + 向量检索 + 大模型问答”，而是围绕 **知识生命周期、知识卡片、断言、证据、知识图谱、混合检索和知识裁决** 构建完整知识基础设施。

## 核心能力

- 数据源、文档、版本和内容单元管理
- 知识抽取：实体、关系、断言、知识卡片
- 知识裁决：重复检测、冲突检测、置信度、人工审核
- 知识发布与版本生命周期
- BM25 / Vector / Card / Claim / Graph 多路召回
- RRF 结果融合与重排序扩展
- 上下文装配与答案引用
- Query Trace 全链路追踪
- LLM、Embedding、Reranker、向量数据库和图数据库可插拔

## 技术栈

- 前端：Vue 3 + Vite + Element Plus
- 后端：Spring Boot 2.7 + Java 8 + MyBatis + MySQL
- AI 服务：Python 3.10 + FastAPI
- 缓存：Redis
- 图数据库：Neo4j（可替换）
- 向量检索：FAISS / Milvus / Qdrant 等（通过适配层扩展）

## 工程结构

```text
llmkb/
├── backend/        # Spring Boot 业务控制面
├── ai-service/     # Python AI 智能计算面
├── frontend/       # Vue 3 管理端
├── docker-compose.yml
├── ARCHITECTURE.md
└── README.md
```

## 快速启动

### 1. 启动基础设施

```bash
docker compose up -d mysql redis neo4j
```

### 2. 启动后端

```bash
cd backend
mvn spring-boot:run
```

### 3. 启动 AI 服务

```bash
cd ai-service
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 12000 --reload
```

### 4. 启动前端

```bash
cd frontend
npm install
npm run dev
```

## 设计原则

- Java 管业务状态和治理。
- Python 管模型推理和检索算法。
- MySQL 管权威事实。
- 向量、全文和图谱索引均为可重建检索视图。
- 模型可以替换，但知识资产、治理流程、权限和检索编排不应绑定具体厂商。

## Repository

https://github.com/jhzhfree/llmkb
