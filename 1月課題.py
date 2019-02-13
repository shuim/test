import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

DICE_NUM=3
VALUE_NUM=2
# STEP1
# 1,2,3番目のサイコロの含有率πの初期値
PI = [0.3,0.5,0.2]

# 1,2,3番目のサイコロの奇数、偶数の目が出る確率(既知)
THETA = [[0.8,0.2],[0.6,0.4],[0.3,0.7]]

# コイン投げの試行回数
N = 10000

# 奇数、偶数の目が出た回数
R = [4746,5254]

# 収束判定用の値
EPS = 1.0e-15

# P(w_i|v_k)事後確率についてi=1,2,3(サイコロの種類) k=1,2(奇数or偶数)
P_wi_vk=[[0 for i in range(2)] for j in range(3)]

# 奇数または偶数が出る確率
P=[0,0]
# 対数尤度（収束判定に用いる）
logP_old = 0
CONV = False


#収束するまでの反復回数
count = 0

while CONV==False:
    PI_old = PI.copy()

    # step2 P(w_i|v_k)の更新
    for k in range(VALUE_NUM):
        denom2 = 0
        for j in range(DICE_NUM):
            denom2 += PI[j]*THETA[j][k]
        for i in range(DICE_NUM):
            P_wi_vk[i][k] = PI[i]*THETA[i][k]/denom2

    # step3-1 π^iの更新
    for i in range(DICE_NUM):
        sum31 = 0
        for k in range(VALUE_NUM):
            sum31 += R[k] * P_wi_vk[i][k]
        PI[i] = sum31/N

    # step3-2-1 更新したπ^iをベイズの定理に代入してP(w_i|v_k)の更新
    for k in range(VALUE_NUM):
        denom321 = 0
        for j in range(DICE_NUM):
            denom321 += PI[j]*THETA[j][k]
        for i in range(DICE_NUM):
            P_wi_vk[i][k] = PI[i]*THETA[i][k]/denom321

    # step3-2-2 3-2-1の更新した値を用いてθ_ikの更新
#    for i in range(DICE_NUM):
#        denom322 = 0
#        for j in range(VALUE_NUM):
#            denom322 += R[j] * P_wi_vk[i][j]
#        for k in range(VALUE_NUM):
#            THETA[i][k] = R[k] * P_wi_vk[i][k] / denom322

    # 式(5.8)でPを計算
    for k in range(VALUE_NUM):
        sum = 0
        for i in range(DICE_NUM):
            sum += PI[i] * THETA[i][k]
        P[k] = sum

    # 式(5.51)で対数尤度を計算
    logP_new = 0
    for k in range(VALUE_NUM):
        logP_new += R[k] * np.log(P[k])
    print(logP_new,logP_old)
    print(PI)

    # 収束判定
    if abs(logP_new - logP_old) < EPS:
        CONV = True
        print(count)

    logP_old = logP_new
    count += 1


