[English](./README.md) | 简体中文

天问一号霍曼转移轨道
========

#### 👽👽👽 使用python模拟天问一号的霍曼转移轨道 👽👽👽 ####

*本项目属于[OGWW](https://github.com/elliottssu/ogww)。*

天问一号火星探测器从地球到火星使用的是改进的[霍曼转移轨道](https://baike.baidu.com/item/%E9%9C%8D%E6%9B%BC%E8%BD%AC%E7%A7%BB%E8%BD%A8%E9%81%93/16295268)（快速转移轨道），起点从地球出发，焦点在出发时地球到到达时火星的直线上的椭圆轨迹。

![Example](./example.png)

## 立即开始 🚀
```bash
$ python3 hohmann.py
```

为了更好的体验，请使用python3.6以上的版本。

## 项目简介
**绘制椭圆轨道思路：**
1. 根据[NASA JPL Horizons](https://ssd.jpl.nasa.gov/?horizons)，我们能够拿到当前行星的运行轨迹及位置数据，所以根据每天的位置数据，可以建立火星与地球的坐标位置。
```python
# 地球/起点
AX = 0.5293788380171227
AY = -0.8669958827267433
```

2. 快速转移轨道的长轴和标准的仍然在同一条直线上，然后再模拟一条椭圆曲线，其中与火星轨道的交点在2021年2月11日附近的坐标。所以根据这个可以确定这个椭圆的圆心、长轴、短轴。
```python
# 两个坐标的差
height = abs(AY-BY)
width = abs(AX-BX)

# 椭圆夹角
angle = math.atan(width/height) * 180 / math.pi

# 2a 长轴长度
aFull = math.sqrt(pow(abs(AX-BX), 2) + pow(abs(AY-BY), 2))

# 斜率 b=0 
k = (AY-BY)/(AX-BX)

# 椭圆中心坐标
centerX = (AX+BX)/2
centerY = k*centerX

```

3. 使用椭圆方程和一元二次方程，求解该曲线上所有的坐标点。

**To do:**
生成点的坐标的X轴两个点的间隔，所对应的椭圆弧长，应该是相等的，这样才能保证匀速。但是这样实现起来会比较麻烦（目前只是粗略的划分间隔）。

**您也可以访问 [https://www.ogww.com/tianwen-1](https://www.ogww.com/tianwen-1) 了解更多项目详情。**
