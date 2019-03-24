import numpy as np

A = np.array([[0.1,0.7,0.2],
             [0.2,0.1,0.7],
             [0.7,0.2,0.1]])

B = np.array([[0.9,0.1],
             [0.6,0.4],
             [0.1,0.9]])

rho = np.array([1/3,1/3,1/3])
# 前向きアルゴリズムの計算結果を格納する配列
alpha = np.zeros((3,3))

alpha[0,0] = rho[0] * B[0,0]
alpha[0,1] = rho[1] * B[1,0]
alpha[0,2] = rho[2] * B[2,0]

#for i in range(3):
#    for j in range(3):
#        alpha[1,j]=