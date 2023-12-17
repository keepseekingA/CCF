from math import sin, cos

"""
m，n<10w,由于时间限制，时间复杂度为（m*n)的方法不考虑。
难点是：把m*n的转化为m+n的
1、先把所有的步骤取出来
2、放缩归放缩，旋转归旋转，各算各的叠加结果
3、最后算出拉伸，在根据旋转公式算。
"""


def solution1():
    n, m = map(int, input().split())
    n_line = []
    for t in range(n):
        n_line.append(list(map(float, input().split())))
    for t in range(m):
        i, j, x, y = map(int, input().split())
        lines = n_line[i-1:j]
        theta = 0
        for line in lines:
            if line[0] == 1:
                k = line[1]
                x *= k
                y *= k
            elif line[0] == 2:
                theta += line[1]
        x0 = x
        y0 = y
        x = x0*cos(theta) - y0*sin(theta)
        y = x0*sin(theta) + y0*cos(theta)
        lines.clear()
        print("{} {}".format(x, y))


def solution2():
    n, m = map(int, input().split())
    k_li = [1.0]
    theta_li = [0]
    for t in range(n):
        _type, _data = map(float, input().split())
        if _type == 1:
            k_li.append(k_li[t] * _data)
            theta_li.append(theta_li[t])
        elif _type == 2:
            k_li.append(k_li[t])
            theta_li.append(theta_li[t] + _data)
    for t in range(m):
        i, j, x0, y0 = map(int, input().split())
        k = k_li[j] / k_li[i-1]
        theta = theta_li[j] - theta_li[i-1]
        x0 *= k
        y0 *= k
        x = x0*cos(theta) - y0*sin(theta)
        y = x0*sin(theta) + y0*cos(theta)
        print("%f %f" % (x, y))



if __name__ == '__main__':
    #solution1()
    solution2()
