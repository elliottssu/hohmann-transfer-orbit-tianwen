# -*- coding: UTF-8 -*-

from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt
import numpy as np

import math

# 地球和火星坐标
AX = 0.5293788380171227
AY = -0.8669958827267433

BX = 0.08648922946393636
BY = 1.559225411955731

# 两个坐标的差
height = abs(AY-BY)
width = abs(AX-BX)

# 椭圆夹角
angle = math.atan(width/height) * 180 / math.pi
print('椭圆旋转角度', angle)

# 2a 长轴长度
aFull = math.sqrt(pow(abs(AX-BX), 2) + pow(abs(AY-BY), 2))

# AB 的半径
radiusA = math.sqrt(pow(abs(AX), 2) + pow(abs(AY), 2))
radiusB = math.sqrt(pow(abs(BX), 2) + pow(abs(BY), 2))

# 斜率
k = (AY-BY)/(AX-BX)
b = BY-k*BX

# 椭圆中心坐标
CX = (AX+BX)/2
CY = k*CX+b
print('椭圆中心坐标', CX, CY)


# 计算理论短长轴
rateBA = 0.63  # 最优距离
bFull = aFull * rateBA
print('长轴和短轴', aFull, bFull)

fig = plt.figure()
ax = fig.add_subplot(111)

# 椭圆和圆画线，其中椭圆 heigh为长轴  angle 为逆时针旋转角度
ell1 = Ellipse(xy=(CX, CY), width=bFull, height=aFull, angle=angle,
               fc='white', ec='red', alpha=0.6, lw=2, linestyle='--')
cir1 = Circle(xy=(0.0, 0.0), radius=radiusA,
              fc='white', ec='blue',  alpha=0.6, lw=2)
cir2 = Circle(xy=(0.0, 0.0), radius=radiusB,
              fc='white', ec='orange',  alpha=0.6, lw=2)

ax.add_patch(ell1)
ax.add_patch(cir1)
ax.add_patch(cir2)

ax.plot(0, 0, 'yo')
ax.plot(CX, CY, 'ro')
plt.axis('scaled')
plt.axis('equal')

x = np.linspace(AX, BX, 2)
y1 = k*x + b
plt.plot(x, y1, linestyle='--', label='起飞到降落距离')

plt.xlim(-2, 2)
plt.ylim(-2, 2)
ax.grid(True)


def equation(x):
    '''
    椭圆方程   参见： 
    旋转+平移： https://math.stackexchange.com/questions/426150/what-is-the-general-equation-of-the-ellipse-that-is-not-in-the-origin-and-rotate
    一元二次方程： https://baike.baidu.com/item/%E4%B8%80%E5%85%83%E4%BA%8C%E6%AC%A1%E6%96%B9%E7%A8%8B/7231190?fr=aladdin 
    '''
    a = aFull/2  # 长轴
    b = bFull/2  # 短轴
    A = angle * math.pi / 180   # 焦点在y轴，逆时针旋转角度

    sin = math.sin
    cos = math.cos
    sqrt = math.sqrt  # 根号

    h = CX
    k = CY

    # 解方程： ay^2+by+c=0  => y=(-b+=sqrt(b^2-4ac))/2a
    # 包含旋转和平移 y轴
    solveA = pow(cos(A)/a, 2) + pow(sin(A)/b, 2)
    solveB = -2*k*pow(cos(A), 2) / pow(a, 2) - (2*(x-h)*sin(A)*cos(A)) / pow(a, 2) - \
        (2*k*pow(sin(A), 2)) / pow(b, 2) + (2*(x-h)*sin(A)*cos(A)) / pow(b, 2)
    solveC = pow((x-h)*sin(A)/a, 2) + pow(k*cos(A)/a, 2) + 2*k*(x-h)*sin(A)*cos(A)/pow(a, 2) + \
        pow((x-h)*cos(A)/b, 2) + pow(k*sin(A)/b, 2) - \
        2*k*(x-h)*sin(A)*cos(A)/pow(b, 2) - 1

    solveDert = pow(solveB, 2) - 4 * solveA * solveC  # b^2-4ac

    # 根据一元二次方程
    if (solveDert < 0):
        print('dert < 0 , 此方程无实根，dert已取正数', x)
        solveDert = -solveDert

    x = x
    y1 = (-solveB + sqrt(solveDert))/(2*solveA)
    y2 = (-solveB - sqrt(solveDert))/(2*solveA)

    yLow = y1 if y1 < y2 else y2
    yHigh = y2 if y2 >= y1 else y1

    return [yLow, yHigh]


def generateRangeCoord():
    '''
    生成轨道坐标 (此间隔为比较粗糙的模拟，未考虑引力及速度影响)
    '''
    xMax = 1.1
    xBegin = AX
    xEnd = BX
    diff = (2 * xMax - xEnd - xBegin) / 102
    diffSplitB = (xMax - xEnd)*0.99

    xCoord = []

    isReturn = False

    xValue = xBegin - diff * 2

    for item in range(102):

        # 控制偏移速度
        vDiff = diff * 2
        if xValue > diffSplitB:
            vDiff = diff * 0.2

        print(xValue, diffSplitB, xValue > diffSplitB, vDiff)

        if isReturn:
            xValue = xValue - vDiff
        else:
            xValue = xValue + vDiff

        if xValue > xMax:
            isReturn = True
            xValue = xMax

        xCoord.append(round(xValue, 16))

    yCoord = []
    xLast = -3
    for item in xCoord:
        if (item > xLast):
            yCoord.append(equation(item)[0])
        else:
            yCoord.append(equation(item)[1])

        xLast = item

    print(xCoord)
    print(yCoord)


# generateRangeCoord()


plt.show()
