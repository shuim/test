import scipy.special as sp
from scipy import integrate
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator,FormatStrFormatter


#ベータ分布のαとβ
alpha = 16
beta =16

# ベータ関数の被積分関数
def integrated_function(u):
    return (u**(alpha-1))*((1-u)**(beta-1))

# ベータ分布の分母
denom = integrate.quad(integrated_function,0,1)

print(denom[0])
# ベータ分布
def beta_distribution(theta,a,b,denom):
    return (theta**(a-1))*((1-theta)**(b-1))/denom[0]

x = np.arange(0,1,0.01)
y = beta_distribution(x,alpha,beta,denom)
#y = (x**(alpha-1))*((1-x)**(beta-1))/denom[0]

#plt.plot(x,y)
#plt.show()

# 面積座標を考える三角形の頂点の座標
x1 = -1/2
y1 = 0
x2 = 1/2
y2 = 0
x3 = 0
y3 = 1

x_1 = np.arange(-1/2,1/2,0.01)
x_1  =np.where(x_1<10,1/2,x_1)
y_1 = np.arange(-1/2,1/2,0.01)
y_1 = np.where(y_1<10,0,y_1)
x_2 = np.arange(-1/2,1/2,0.01)
x_2 = np.where(x_2<10, 1/2,x_2)
y_2 = np.arange(-1/2,1/2,0.01)
y_2 = np.where(y_2<10,0,y_2)
x_3 = np.arange(-1/2,1/2,0.01)
x_3 = np.where(x_3<10, 0,x_3)
y_3 = np.arange(-1/2,1/2,0.01)
y_3 = np.where(y_3<10,1,y_3)

#三角形の外ならz=0
def check(X,Y):
    if (Y <= (2 * X + 1)) & (Y <= (-2 * X + 1)) & (Y >= 0):
        return 1
    else:
        return 0

#三角形内の3点の座標を与えると面積を返す関数
def square(x_1,y_1,x_2,y_2,x_3,y_3):
    a = np.sqrt((x_2 - x_3) ** 2 + (y_2 - y_3) ** 2)
    b = np.sqrt((x_1 - x_3) ** 2 + (y_1 - y_3) ** 2)
    c = np.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
    # ヘロンの公式
    s = (a + b + c) / 2
    return np.sqrt(s * (s - a) * (s - b) * (s - c))

n = square(x1,y1,x2,y2,x3,y3)


alpha_1 = 2
alpha_2 = 4
alpha_3 = 6
alpha = alpha_1+alpha_2+alpha_3-3

coef = sp.gamma(alpha)/sp.gamma(alpha_1)*sp.gamma(alpha_2)*sp.gamma(alpha_3)


# Make data

fig = plt.figure()
ax = fig.gca(projection = '3d')

# Make data
X = np.arange(-1/2,1/2,0.01)
Y = np.arange(0,1,0.01)
X,Y = np.meshgrid(X,Y)

#    theta_1 = square(X, Y, x_2, y_2, x_3, y_3) / n
#    theta_2 = square(x_1, y_1, X, Y, x_3, y_3) / n
#    theta_3 = square(x_1, y_1, x_2, y_2, X, Y) / n
#    Z = coef * theta_1**(alpha_1-1) * theta_2**(alpha_2-1) * theta_3**(alpha_3-1)
#else:
#    Z = 0
theta_1 = square(X,Y, x_2, y_2, x_3, y_3) / n
theta_2 = square(x_1, y_1, X, Y, x_3, y_3) / n
theta_3 = square(x_1, y_1, x_2, y_2, X, Y) / n

print(alpha_1)
print(coef)
#print(theta_2)
#print(theta_3)

Z = (theta_1**(alpha_1-1)) * (theta_2**(alpha_2-1)) * (theta_3**(alpha_3-1))
print(X)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(-0.1,0.3)

plt.show()