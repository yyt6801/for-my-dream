import numpy as np
import matplotlib.pyplot as plt


# #################################拟合优度R^2的计算######################################
def __sst(y_no_fitting):
    """
    计算SST(total sum of squares) 总平方和
    :param y_no_predicted: List[int] or array[int] 待拟合的y
    :return: 总平方和SST
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list =[(y - y_mean)**2 for y in y_no_fitting]
    sst = sum(s_list)
    return sst


def __ssr(y_fitting, y_no_fitting):
    """
    计算SSR(regression sum of squares) 回归平方和
    :param y_fitting: List[int] or array[int]  拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 回归平方和SSR
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list =[(y - y_mean)**2 for y in y_fitting]
    ssr = sum(s_list)
    return ssr


def __sse(y_fitting, y_no_fitting):
    """
    计算SSE(error sum of squares) 残差平方和
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 残差平方和SSE
    """
    s_list = [(y_fitting[i] - y_no_fitting[i])**2 for i in range(len(y_fitting))]
    sse = sum(s_list)
    return sse


def goodness_of_fit(y_fitting, y_no_fitting):
    """
    计算拟合优度R^2
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 拟合优度R^2
    """
    SSR = __ssr(y_fitting, y_no_fitting)
    SST = __sst(y_no_fitting)
    rr = SSR /SST
    return rr



# 拟合数据集
x_arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33])
y_arr = np.array([-3,-1,1,2,3,3,4,4,1,2,1,-1,-1,0,-1,0,0,-1,0,-1,-3,0,2,-2,-1,-1,-1,-2,-1,-3,-2,5,10])

figure1 = plt.figure(figsize=(8, 6))
# coeff 为系数，poly_fit 拟合函数
# 1. 先拟合获取系数
coeff_1 = np.polyfit(x_arr, y_arr, 1)
print("一阶拟合系数为:", coeff_1)
# 2. 根据系数得到多项式
poly_fit_1 = np.poly1d(coeff_1)
print("一阶多项式为:", poly_fit_1)
# 3. 输入变量(单个值或者变量数组)，得到拟合结果(数组)
y_fit_1 = poly_fit_1(x_arr)
print("一阶拟合得到的数据为: ", y_fit_1)
# 4. 根据结果作图
plt.plot(x_arr, y_fit_1, 'green',label="一阶拟合")
# 5. 根据原始数据以及拟合数据得到拟合优度
rr1 = goodness_of_fit(y_fit_1, y_arr)
print("一阶拟合优度为%.5f" % rr1)
#
coeff_2 = np.polyfit(x_arr, y_arr, 2)
print("二阶拟合系数为:", coeff_2)
poly_fit_2 = np.poly1d(coeff_2)
print("二阶多项式为:", poly_fit_2)
y_fit_2 = poly_fit_2(x_arr)
print("二阶拟合得到的数据为: ", y_fit_2)
plt.plot(x_arr, y_fit_2, 'orange',label="二阶拟合")
rr2 = goodness_of_fit(y_fit_2, y_arr)
print("二阶拟合优度为%.5f" % rr2)
# #
coeff_3 = np.polyfit(x_arr, y_arr, 3)
print("三阶拟合系数为:", coeff_3)
poly_fit_3 = np.poly1d(coeff_3)
print("三阶多项式为:", poly_fit_3)
y_fit_3 = poly_fit_3(x_arr)
print("三阶拟合得到的数据为: ", y_fit_3)
plt.plot(x_arr, poly_fit_3(x_arr), 'skyblue',label="三阶拟合")
rr3 = goodness_of_fit(y_fit_3, y_arr)
print("三阶拟合优度为%.5f" % rr3)
# #
coeff_4 = np.polyfit(x_arr, y_arr, 4)
print("四阶拟合系数为:", coeff_4)
poly_fit_4 = np.poly1d(coeff_4)
print("四阶多项式为:", poly_fit_4)
y_fit_4 = poly_fit_4(x_arr)
print("四阶拟合得到的数据为: ", y_fit_4)
plt.plot(x_arr, y_fit_4, 'blue',label="四阶拟合")
rr4 = goodness_of_fit(y_fit_4, y_arr)
print("四阶拟合优度为%5f" % rr4)
#
coeff_5 = np.polyfit(x_arr, y_arr, 5)
print("五阶拟合系数为:", coeff_5)
poly_fit_5 = np.poly1d(coeff_5)
print("五阶多项式为:", poly_fit_5)
y_fit_5 = poly_fit_5(x_arr)
print("五阶拟合得到的数据为: ", y_fit_5)
plt.plot(x_arr, y_fit_5, 'red', label="五阶拟合")
rr5 = goodness_of_fit(y_fit_5, y_arr)
print("五阶拟合优度为%.5f" % rr5)

plt.scatter(x_arr, y_arr, color='black', label="原始数据")
plt.title("1~5阶拟合曲线图")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.legend(loc=2)
plt.show()