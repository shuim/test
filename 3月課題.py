# json形式のファイルでテキストの行列A,B,ρのファイル名、サイズを指定するようにする
# A,B,rhoの初期状態をcsvで設定するようにする。
import json
import csv

# json形式の設定ファイルで読みたい項目
setting_list = ["n_observations","n_dicevalues","n_dicetypes",
                "A_matrixfile","B_matrixfile","Rho_vectorfile"]

ID_N_OBSERVATIONS = 0
ID_N_DICEVALUES = 1
ID_N_DICETYPES = 2
ID_A_MATRIXFILE = 3
ID_B_MATRIXFILE = 4
ID_RHO_VECTORFILE = 5

"""
変数について
n_obs:サイコロを投げる試行の観測回数
n_dicevals:サイコロがとりうる値の数
n_dicetypes:サイコロの種類
A_filename:行列Aの設定があるcsvファイル名
B_filename:行列Bの設定があるcsvファイル名
Rho_filename:ベクトルρの設定があるcsvファイル名
"""


# json形式の設定ファイル(setting.json)を読む
def read_setting(read_data):
    f = open("setting.json",'r')

    json_data = json.load(f)
    n_obs = json_data[setting_list[ID_N_OBSERVATIONS]]
    n_dicevals = json_data[setting_list[ID_N_DICEVALUES]]
    n_dicetypes = json_data[setting_list[ID_N_DICETYPES]]
    A_filename = json_data[setting_list[ID_A_MATRIXFILE]]
    B_filename = json_data[setting_list[ID_B_MATRIXFILE]]
    Rho_filename = json_data[setting_list[ID_RHO_VECTORFILE]]
    read_data.append(n_obs)
    read_data.append(n_dicevals)
    read_data.append(n_dicetypes)
    read_data.append(A_filename)
    read_data.append(B_filename)
    read_data.append(Rho_filename)

# csvファイルからA行列、B行列、ベクトルρの情報を取ってくる
def read_and_set_A_B_Rho(A,B,Rho,data):
    print(data[ID_A_MATRIXFILE])
    with open(data[ID_A_MATRIXFILE]) as fpA:
        A = list(csv.reader(fpA))
    with open(data[ID_B_MATRIXFILE]) as fpB:
        B = list(csv.reader(fpB)).copy()
    with open(data[ID_RHO_VECTORFILE]) as fpRho:
        Rho = list(csv.reader(fpRho)).copy()
    print(A)
    print(B)
    print(Rho)
    A = [[float(elm) for elm in v] for v in A]
    print(A)

    Rho = [[float(elm) for elm in v] for v in Rho]
    print(Rho)



if __name__ == "__main__":
    read_data = []
    read_setting(read_data)
    A = []
    B = []
    Rho = []
    read_and_set_A_B_Rho(A=A,B=B,Rho=Rho,data=read_data)







# 前向きアルゴリズムの実装自体は簡単なので後回し
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

