# 扩展点

建议下一阶段继续抽象并实现：
- LlmProvider
- EmbeddingProvider
- RerankProvider
- VectorStoreProvider
- FullTextSearchProvider
- GraphProvider
- ObjectStoreProvider
- DocumentParser
- PermissionFilter

所有检索器必须在召回前执行 ACL；所有知识必须保留 Source -> Evidence -> Claim -> Knowledge/Card 的可追溯链。
