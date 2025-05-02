import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
import lightgbm as lgb
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.neural_network import MLPRegressor

from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score
import matplotlib.pyplot as plt
import joblib
import os

if __name__ == '__main__':
    df = pd.read_csv(r'PROCESSING_MODEL（训练用）.csv')

    # 异常值处理
    for column in ["GAL_DATA_TOKN_PRESET", "GAL_DATA_TOKN_DISSET", "GAL_DATA_KNHE_DRS_ACT", "GAL_DATA_TOKN_ANGACT", "GAL_DATA_LISP_ACT", "GAL_DATA_STRI_THI","GAL_DATA_STWD_NEX","GAL_DATA_COATINGCODE"]:
        # 将无法转换为数值的数据替换为NaN
        df[column] = pd.to_numeric(df[column], errors='coerce')
    # 删除包含NaN的行
    df.dropna(inplace=True)

    # 划分训练集和测试集
    train_ratio = 0.8
    test_ratio = 0.2
    train_data, test_data = train_test_split(df, test_size=test_ratio, random_state=42)

    # 从DataFrame中提取特征和目标列"Label"  
    X_train = train_data[["TOTALWEIGHT_ACT", "GAL_DATA_TOKN_DISSET", "GAL_DATA_KNHE_DRS_ACT","GAL_DATA_TOKN_ANGACT","GAL_DATA_LISP_ACT", "GAL_DATA_STRI_THI","GAL_DATA_STWD_NEX","GAL_DATA_COATINGCODE" ]]
    y_train = train_data["GAL_DATA_TOKN_PRESET"]

    X_test = test_data[["TOTALWEIGHT_ACT", "GAL_DATA_TOKN_DISSET", "GAL_DATA_KNHE_DRS_ACT", "GAL_DATA_TOKN_ANGACT","GAL_DATA_LISP_ACT", "GAL_DATA_STRI_THI", "GAL_DATA_STWD_NEX","GAL_DATA_COATINGCODE"]]
    y_test = test_data["GAL_DATA_TOKN_PRESET"]

    # 训练LightGBM回归模型
    lgb_model = lgb.LGBMRegressor()
    lgb_model.fit(X_train, y_train)

    # 使用模型进行预测
    y_pred_lgb = lgb_model.predict(X_test)

    # 评估模型性能
    # 计算R方
    r2_lgb = r2_score(y_test, y_pred_lgb)
    mse = mean_squared_error(y_test, y_pred_lgb)
    mae = mean_absolute_error(y_test, y_pred_lgb)

    # 输出R方
    print("LightGBM回归模型的R方 (R-squared):", r2_lgb)
    print("LightGBM回归模型的均方误差 (MSE):", mse)
    print("LightGBM回归模型的平均绝对误差 (MAE):", mae)
   
    
    # 训练随机森林回归模型
    rf_model = RandomForestRegressor(n_estimators=278, max_depth=38, min_samples_split=2, min_samples_leaf=1,max_features=0.8,random_state=42)
    rf_model.fit(X_train, y_train)
    
    y_pred_rf = rf_model.predict(X_test)
    
    # 计算R方
    r2_rf = r2_score(y_test, y_pred_rf)
    mse = mean_squared_error(y_test, y_pred_rf)
    mae = mean_absolute_error(y_test, y_pred_rf)

    # 输出R方
    print("随机森林模型的R方 (R-squared):", r2_rf)
    print("随机森林模型的均方误差 (MSE):", mse)
    print("随机森林模型的平均绝对误差 (MAE):", mae)
    
    # 训练线性回归模型
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    # 使用模型进行预测
    y_pred_lr = lr_model.predict(X_test)
    # 计算R方、均方误差和平均绝对误差
    r2_lr = r2_score(y_test, y_pred_lr)
    mse = mean_squared_error(y_test, y_pred_lr)
    mae = mean_absolute_error(y_test, y_pred_lr)
    # 输出结果
    print("线性回归模型的R方 (R-squared):", r2_lr)
    print("线性回归模型的均方误差 (MSE):", mse)
    print("线性回归模型的平均绝对误差 (MAE):", mae)
    
    # 训练KNN模型
    knn_model = KNeighborsRegressor(n_neighbors=5)
    knn_model.fit(X_train, y_train)
    # 使用模型进行预测
    y_pred_knn = knn_model.predict(X_test)
    # 计算R方、均方误差和平均绝对误差
    r2_knn = r2_score(y_test, y_pred_knn)
    mse = mean_squared_error(y_test, y_pred_knn)
    mae = mean_absolute_error(y_test, y_pred_knn)
    # 输出结果
    print("KNN模型的R方 (R-squared):", r2_knn)
    print("KNN模型的均方误差 (MSE):", mse)
    print("KNN模型的平均绝对误差 (MAE):", mae)
    
    # 训练SVM模型
    svm_model = SVR()
    svm_model.fit(X_train, y_train)
    # 使用模型进行预测
    y_pred_svm = svm_model.predict(X_test)
    # 计算R方、均方误差和平均绝对误差
    r2_svm = r2_score(y_test, y_pred_svm)
    mse = mean_squared_error(y_test, y_pred_svm)
    mae = mean_absolute_error(y_test, y_pred_svm)
    # 输出结果
    print("SVM模型的R方 (R-squared):", r2_svm)
    print("SVM模型的均方误差 (MSE):", mse)
    print("SVM模型的平均绝对误差 (MAE):", mae)
    
    # 训练XGBoost模型
    xgb_model = XGBRegressor()
    xgb_model.fit(X_train, y_train)
    # 使用模型进行预测
    y_pred_xgb = xgb_model.predict(X_test)
    # 计算R方、均方误差和平均绝对误差
    r2_xgb = r2_score(y_test, y_pred_xgb)
    mse = mean_squared_error(y_test, y_pred_xgb)
    mae = mean_absolute_error(y_test, y_pred_xgb)
    # 输出结果
    print("XGBoost模型的R方 (R-squared):", r2_xgb)
    print("XGBoost模型的均方误差 (MSE):", mse)
    print("XGBoost模型的平均绝对误差 (MAE):", mae)
    
    # 训练CatBoost模型
    cat_model = CatBoostRegressor(verbose=0)
    cat_model.fit(X_train, y_train)
    # 使用模型进行预测
    y_pred_cat = cat_model.predict(X_test)
    # 计算R方、均方误差和平均绝对误差
    r2_cat = r2_score(y_test, y_pred_cat)
    mse = mean_squared_error(y_test, y_pred_cat)
    mae = mean_absolute_error(y_test, y_pred_cat)
    # 输出结果
    print("CatBoost模型的R方 (R-squared):", r2_cat)
    print("CatBoost模型的均方误差 (MSE):", mse)
    print("CatBoost模型的平均绝对误差 (MAE):", mae)
    
    # 训练神经网络模型：使用了MLPRegressor类来创建一个多层感知器（Multi-Layer Perceptron）模型。hidden_layer_sizes参数指定了隐藏层的神经元数量，activation参数指定了激活函数，solver参数指定了优化算法，max_iter参数指定了最大迭代次数。
    nn_model = MLPRegressor(hidden_layer_sizes=(100, 50), activation='relu', solver='adam', max_iter=1000)
    nn_model.fit(X_train, y_train)
    # 使用模型进行预测
    y_pred_nn = nn_model.predict(X_test)
    # 计算R方、均方误差和平均绝对误差
    r2_nn = r2_score(y_test, y_pred_nn)
    mse = mean_squared_error(y_test, y_pred_nn)
    mae = mean_absolute_error(y_test, y_pred_nn)
    # 输出结果
    print("神经网络模型的R方 (R-squared):", r2_nn)
    print("神经网络模型的均方误差 (MSE):", mse)
    print("神经网络模型的平均绝对误差 (MAE):", mae)