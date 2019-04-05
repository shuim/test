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
def read_and_set_A_B_Rho(A=[],B=[],Rho=[],data=[]):
    with open(data[ID_A_MATRIXFILE]) as fpA:
        A = list(csv.reader(fpA))
    with open(data[ID_B_MATRIXFILE]) as fpB:
        B = list(csv.reader(fpB)).copy()
    with open(data[ID_RHO_VECTORFILE]) as fpRho:
        Rho = list(csv.reader(fpRho)).copy()

    return A,B,Rho

# 中身を数値に変換できる配列の中身を数値に変換する. 配列の次元を指定
def conv_float(l,dim):
    if dim==1:
        l = [float(s) for s in l]
    if dim==2:
        l = [[float(elm) for elm in v]for v in l]
    return l




# 前向きアルゴリズムで確率を計算
# sは教科書に倣い観測結果の配列を表すものとする。
def forward_algorithm(A,B,Rho=[],s=[]):
    # 戻り値の確率
    p = 0
    # Step1 初期化 s[0]は観測結果の最初の値 教科書のα
    alpha = [Rho[i]*B[i][s[0]] for i in range(len(Rho))]
    # Step2 再帰的計算
    for t in range(1,len(s)):
        old_alpha = alpha.copy()
        for j in range(len(Rho)):
            sum = 0
            for i in range(len(Rho)):
                sum += old_alpha[i] * A[i][j]
            alpha[j] = sum * B[j][s[t]]
        #print(t,alpha)


    # Step3 確率の計算
    for i in range(len(Rho)):
        p += alpha[i]
    return p





if __name__ == "__main__":
    read_data = []
    # setting.jsonから設定を読む
    read_setting(read_data)
    # csvファイルのA,B行列、ρベクトルのデータを代入
    A,B,Rho = read_and_set_A_B_Rho(data=read_data)
    # 数値に変換できる配列を変換する
    A = conv_float(A,dim=2)
    B = conv_float(B,dim=2)
    # 応急処置
    Rho=Rho[0]
    Rho = conv_float(Rho,dim=1)

    # 前向きアルゴリズムで今回の問題(s=[0,1,0] 0:奇数、1:偶数)
    p = forward_algorithm(A,B,Rho,s = [0,1,0])

    with open("result.txt",mode='w') as f:
        f.write("前向きアルゴリズムによる確率:%f" %p)

