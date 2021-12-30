list1 = [ [[[[] for l in range(5)] for k in range(4)] for j in range(3)] for i in range(2)]
# 赋值也可以这样
# list1[0][0][0][0].append(0)
# list1[0][0][0][1].append(1)

for i in range(2):
    for j in range(3):
        for k in range(4):
            for l in range(5):
                list1[i][j][k][l] = i*1000 + j*100 + k*10 +l

for i in range(2):
    for j in range(3):
        for k in range(4):
            for l in range(5):
                print(list1[i][j][k][l])