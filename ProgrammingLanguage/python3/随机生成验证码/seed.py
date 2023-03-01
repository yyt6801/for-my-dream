import numpy as np
 
np.random.seed(1)
L1 = np.random.randn(3, 3)
# np.random.seed(1) # 同一种子同一堆结果不同，同样种子不同堆结果一样
L2 = np.random.randn(3, 3)
print(L1)
print(L2)