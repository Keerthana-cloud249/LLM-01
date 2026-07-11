from src.embedding import Embedding
embedding=Embedding(10,4)
vectors=embedding.lookup([1,3,5])
print(vectors)
print(vectors.shape)
print(embedding.embedding_matrix.shape)
print(embedding.lookup([1]).shape)
print(embedding.lookup([1,2,3,4,5]).shape)
