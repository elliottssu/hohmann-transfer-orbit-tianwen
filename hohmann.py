# -*- coding: UTF-8 -*-

from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt
import numpy as np
import util

# 地球/起点
AX = 0.5293788380171227
AY = -0.8669958827267433

# 霍曼转移理论火星位置
H_BX = -0.814
H_BY = (AY/AX) * H_BX
H_aFull, H_bFull, H_centerX, H_centerY, H_angle, radiusA, H_radiusB, H_slope = util.ellipseCoord(
    AX, AY, H_BX, H_BY, 0.9)

# 快速转移理论火星位置
F_BX = -1
F_BY = (AY/AX) * F_BX
F_aFull, F_bFull, F_centerX, F_centerY, F_angle, radiusA, F_radiusB, F_slope = util.ellipseCoord(
    AX, AY, F_BX, F_BY, 0.85)


# 快速转移理论椭圆长轴终点
DX = 0.35
DY = 1.52

EX = 0.08648922946393636
EY = 1.559225411955731


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('TianWen 1 Orbit Simulation - OGWW.COM', fontsize=12, color='k')

# 椭圆和圆画线，其中椭圆 heigh为长轴  angle 为逆时针旋转角度
ell1 = Ellipse(xy=(H_centerX, H_centerY), width=H_bFull, height=H_aFull, angle=H_angle,
               fc='white', fill=False, ec='grey', lw=1, linestyle='--', label='Hohmann transfer orbit')
ell2 = Ellipse(xy=(F_centerX, F_centerY), width=F_bFull, height=F_aFull, angle=F_angle,
               fc='white', fill=False, ec='red', lw=1, linestyle='--', label='Fast transfer orbit')
cir1 = Circle(xy=(0.0, 0.0), radius=radiusA,
              fc='white', fill=False, ec='#8e8eec', lw=2, label='Earth')
cir2 = Circle(xy=(0.0, 0.0), radius=H_radiusB,
              fc='white', fill=False, ec='orange', lw=2, label='Mars')
F_X = np.linspace(AX, F_BX, 2)
F_Y = F_slope * F_X
plt.plot(F_X, F_Y, linestyle='--', lw=1,
         color='red', alpha=0.6, label='Orbit axis')

ax.add_patch(ell1)
ax.add_patch(ell2)
ax.add_patch(cir1)
ax.add_patch(cir2)
ax.plot(0, 0, 'bo')
ax.plot(F_centerX, F_centerY, 'ro')
plt.axis('scaled')
plt.axis('equal')
plt.xlim(-2.8, 2.8)
plt.ylim(-2.8, 2.8)
plt.legend(fontsize="xx-small")
ax.plot(AX, AY, 'k*')
ax.annotate('Start', xy=(AX, AY), xytext=(AX+0.1, AY-0.2))
ax.plot(DX, DY, 'k*')
ax.annotate('End', xy=(DX, DY), xytext=(DX+0.1, DY+0.1))
ax.set_ylim(-2, 2)
ax.grid(True)

# 生成轨道数据
# util.generateRangeCoord(AX, EX, F_aFull, F_bFull,
#                         F_angle, F_centerX, F_centerY)


plt.show()
