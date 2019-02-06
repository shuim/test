import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

DICE_NUM=3
VALUE_NUM=2
# STEP1
# 1,2,3番目のサイコロの含有率πの初期値
PI = [0.3,0.5,0.2]
PINEW = [0,0,0]

# 1,2,3番目のサイコロの奇数、偶数の目が出る確率(既知)
THETA = [[0.8,0.2],[0.6,0.4],[0.3,0.7]]

# コイン投げの試行回数
N = 10000

# 奇数、偶数の目が出た回数
R = [4746,5254]

# 収束判定用の値
EPS = 1.0e-8

# P(w_i|v_k)事後確率についてi=1,2,3(サイコロの種類) k=1,2(奇数or偶数)
P_wi_vk=[[0 for i in range(2)] for j in range(3)]
#P_wi_vk=[[0,0],[0,0],[0,0]]


# step2 P(w_i|v_k)の更新
for i in range(DICE_NUM):
    for k in range(VALUE_NUM):
        P_wi_vk[i][k] = PI[i]*THETA[i][k]


# step3-1 π^iの更新
for i in range(DICE_NUM):
    for k in range(VALUE_NUM):
        PINEW[i] = 1/N*(R[k]*P_wi_vk[i][k])


# step3-2 更新したπ^iをベイズの定理に代入してP(w_i|v_k)の更新
#P_wi_vk_NEW =
