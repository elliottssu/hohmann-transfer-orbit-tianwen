# -*- coding: UTF-8 -*-

import math

def ellipseCoord(AX, AY, BX, BY, rateBA):
    '''
    椭圆坐标
    BX: A对对立坐标X轴
    BY: A对对立坐标Y轴
    rateBA: 长轴与短轴之间的比率
    '''

    # 两个坐标的差
    height = abs(AY-BY)
    width = abs(AX-BX)

    # 椭圆夹角
    angle = math.atan(width/height) * 180 / math.pi

    # 2a 长轴长度
    aFull = math.sqrt(pow(abs(AX-BX), 2) + pow(abs(AY-BY), 2))

    # A和B 的半径
    radiusA = math.sqrt(pow(abs(AX), 2) + pow(abs(AY), 2))
    radiusB = math.sqrt(pow(abs(BX), 2) + pow(abs(BY), 2))

    # 斜率 b=0 
    k = (AY-BY)/(AX-BX)

    # 椭圆中心坐标
    centerX = (AX+BX)/2
    centerY = k*centerX

    # 计算理论短长轴
    bFull = aFull * rateBA

    print('椭圆旋转角度', angle)
    print('椭圆中心坐标', centerX, centerY)
    print('长轴和短轴', aFull, bFull)

    return aFull, bFull, centerX, centerY, angle, radiusA, radiusB, k


def equation(x, aFull, bFull, angle, CX, CY):
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

    solveDelta = pow(solveB, 2) - 4 * solveA * solveC  # b^2-4ac


    # 根据一元二次方程
    if (solveDelta < 0):
        print('警告：Delta < 0 , 此方程无实根，Delta已取正数', x)
        solveDelta = -solveDelta

    x = x
    y1 = (-solveB + sqrt(solveDelta))/(2*solveA)
    y2 = (-solveB - sqrt(solveDelta))/(2*solveA)

    yLow = y1 if y1 < y2 else y2
    yHigh = y2 if y2 >= y1 else y1

    return [yLow, yHigh]

# To do
# Divide the length of each segment equally according to the circumference of the ellipse
def generateRangeCoord(AX, BX, aFull, bFull, angle, CX, CY):
    '''
    生成轨道坐标 (此间隔为比较粗糙的模拟，未考虑引力及速度影响)
    '''
    rangeCount = 102 # 开始与结束时间约为102天
    xMax = 1.0753
    xBegin = AX
    xEnd = BX
    diff = (2 * xMax - xEnd - xBegin) / rangeCount
    diffSplitA = xMax*0.99
    diffSplitB = xMax*0.95
    diffSplitC = xMax*0.9

    xCoord = []

    isReturn = False

    xValue = xBegin - diff

    for item in range(rangeCount):

        # 控制偏移速度
        vDiff = diff
        if xValue > diffSplitC:
            vDiff = diff * 0.7
        if xValue > diffSplitB:
            vDiff = diff * 0.5
        if xValue > diffSplitA:
            vDiff = diff * 0.20

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
            yCoord.append(equation(item, aFull, bFull, angle, CX, CY)[0])
        else:
            yCoord.append(equation(item, aFull, bFull, angle, CX, CY)[1])

        xLast = item

    print(xCoord)
    print(yCoord)

