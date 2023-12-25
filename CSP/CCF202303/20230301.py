if __name__ == '__main__':
    area = 0
    n, a, b = map(int, input().split())     # n:田地块数  a,b：总区域右上角坐标
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())      # 该块田地的左下角坐标，右上角坐标
        if x1 < 0:
            x1 = 0
        elif x1 >= a:
            continue
        if y1 < 0:
            y1 = 0
        elif y1 >= b:
            continue
        if x2 > a:
            x2 = a
        elif x2 <= 0:
            continue
        if y2 > b:
            y2 = b
        elif y2 <= 0:
            continue
        area += (x2 - x1) * (y2 - y1)       # 累加田地的面积
    print(area)
