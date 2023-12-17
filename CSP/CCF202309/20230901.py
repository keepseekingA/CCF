def solution1():
    str_list = input().split(" ")
    n = eval(str_list[0])
    m = eval(str_list[1])
    n_list = []
    res_list = []
    while n > 0:
        n_list.append(input().split(" "))
        n -= 1
    while m > 0:
        temp = input().split(" ")
        m_list = [eval(i) for i in temp]
        for t in n_list:
            m_list[0] += eval(t[0])
            m_list[1] += eval(t[1])
        res_list.append(m_list)
        m -= 1
    for coord in res_list:
        print("{} {}".format(coord[0], coord[1]))


def solution2():
    n, m = map(int, input().split(" "))
    t_x = t_y = 0
    for i in range(n):
        x1, y1 = map(int, input().split(" "))
        t_x += x1
        t_y += y1
    for i in range(m):
        x, y = map(int, input().split(" "))
        x += t_x
        y += t_y
        print("%d %d" % (x, y))


def solution3():
    n, m = map(int, input().split())
    temp_x = temp_y = 0
    for i in range(n):
        x1, y1 = map(int, input().split())
        temp_x += x1
        temp_y += y1
    for i in range(m):
        x, y = map(int, input().split())
        x += temp_x
        y += temp_y
        print('{} {}'.format(x, y))


if __name__ == "__main__":
    solution2()