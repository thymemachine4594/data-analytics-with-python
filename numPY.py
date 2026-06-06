import numpy as np
a=np.array([1,2,3])
b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]],dtype=bool)
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)
print(b.itemsize)