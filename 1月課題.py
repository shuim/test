import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 1,2,3番目のサイコロの含有率πの初期値
PI_1 = 0.3
PI_2 = 0.5
PI_3 = 0.2

# 1,2,3番目のサイコロの奇数の目が出る確率
THETA_11 = 0.8
THETA_21 = 0.6
THETA_31 = 0.3

STEP = 10000

# 奇数、偶数の目が出た回数
R1 = 4746
R2 = 5254

# 収束判定用の値
CONV = 0.001

