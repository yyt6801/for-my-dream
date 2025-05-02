import numpy as np

# 定义适应度函数（例如，简单的二次函数）
def fitness_function(x):
    return x**2  # 目标是最小化这个函数

# 初始化参数
N = 30  # 种群规模
MaxIter = 100  # 最大迭代次数
lb = -10  # 搜索空间下界
ub = 10   # 搜索空间上界

# 初始化灰狼位置
wolves = np.random.uniform(lb, ub, (N, 1))

# 初始化α, β, δ狼
alpha, beta, delta = wolves[np.argmin([fitness_function(wolf) for wolf in wolves])], None, None
indices = np.argsort([fitness_function(wolf) for wolf in wolves])
if len(indices) > 1: beta = wolves[indices[1]]
if len(indices) > 2: delta = wolves[indices[2]]

# 迭代更新
for t in range(MaxIter):
    a = 2 - t * (2 / MaxIter)  # 线性递减的a
    for i in range(N):
        r1, r2 = np.random.rand(), np.random.rand()
        A1, C1 = 2 * a * r1 - a, 2 * r2
        D_alpha = np.abs(C1 * alpha - wolves[i])
        X1 = alpha - A1 * D_alpha
        
        r1, r2 = np.random.rand(), np.random.rand()
        A2, C2 = 2 * a * r1 - a, 2 * r2
        D_beta = np.abs(C2 * beta - wolves[i])
        X2 = beta - A2 * D_beta
        
        r1, r2 = np.random.rand(), np.random.rand()
        A3, C3 = 2 * a * r1 - a, 2 * r2
        D_delta = np.abs(C3 * delta - wolves[i])
        X3 = delta - A3 * D_delta
        
        wolves[i] = (X1 + X2 + X3) / 3
    
    # 更新α, β, δ狼
    fitness_values = [fitness_function(wolf) for wolf in wolves]
    alpha, beta, delta = wolves[np.argmin(fitness_values)], None, None
    indices = np.argsort(fitness_values)
    if len(indices) > 1: beta = wolves[indices[1]]
    if len(indices) > 2: delta = wolves[indices[2]]
    print(t, alpha, fitness_function(alpha))

# 输出最优解
optimal_solution = alpha
print(f"Optimal Solution: {optimal_solution}, Fitness Value: {fitness_function(optimal_solution)}")