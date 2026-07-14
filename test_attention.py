from src.attention import Attention
import numpy as np
attention= Attention (64,32)
X=np.random.randn(5,64)
output=attention.compute_attention(X)
print(output)
print(output.shape)
print("Input shape:", X.shape)

print("W_Q:", attention.W_Q.shape)
print("W_K:", attention.W_K.shape)
print("W_V:", attention.W_V.shape)

print("Output shape:", output.shape)