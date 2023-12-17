def solution1(n):
    str_li = []
    for i in range(n*8):
        site = int(i/8)
        if i % 8 == 0:
            str_li.append("")
        str_li[site] += input()
    num = [1]
    for i in range(1, n):
        t = 1
        now = str_li[i]
        for item in str_li[0:i]:
            if item == now:
                t += 1
        num.append(t)
    for u in num:
        print(u)

    print(str_li)


def solution2():
    n = int(input())
    chess = {}
    for i in range(n):
        tmp = ''
        for j in range(8):
            tmp += input()
        if tmp not in chess:
            chess[tmp] = 1
        else:
            chess[tmp] += 1
        print(chess[tmp])


if __name__ == "__main__":
    n = eval(input())
    if n > 0:
        solution1(n)
    # solution2()
