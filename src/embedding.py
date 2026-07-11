import numpy as np
class Embedding:

    def __init__(self,vocab_size,embedding_dimension):
        self.vocab_size=vocab_size
        self.embedding_dimension=embedding_dimension
        
        self.embedding_matrix =np.random.randn(vocab_size,embedding_dimension)

    def lookup(self,token_ids):
        vectors=[]
        for token_id in token_ids:
            vectors.append(self.embedding_matrix[token_id])
        return np.array(vectors)

