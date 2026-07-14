import numpy as np
class Attention:
    def __init__(self,embedding_dimension,attention_dimension):
        self.embedding_dimension= embedding_dimension
        self.attention_dimension= attention_dimension
        self.W_Q=np.random.randn(embedding_dimension,attention_dimension)
        self.W_K=np.random.randn(embedding_dimension,attention_dimension)
        self.W_V=np.random.randn(embedding_dimension,attention_dimension)
    def softmax(self,scores):
        scores=scores-np.max(scores)
        exp_scores=np.exp(scores)
        return exp_scores/np.sum(exp_scores,axis=1,keepdims=True)
    def compute_attention(self,X):
        Q=X @ self.W_Q
        K=X @ self.W_K
        V=X @ self.W_V

        scores=Q @ K.T
        scores=scores/np.sqrt(self.attention_dimension)

        attention_weights=self.softmax(scores)
        output=attention_weights @ V
        return output