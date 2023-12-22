def d_add(v1, v2, x):   # +法求导
    return 1 if v1 == x or v2 == x else 0


def d_sub(v1, v2, x):   # -法求导
    if v1 == x:
        return 1
    elif v2 == x:
        return -1
    else:
        return 0


def d_mas(v1, v2, x_value):     # *法求导
    x = "x" + str(x_value[0])
    if v1 == x and v2 != x:
        return v2
    elif v2 == x and v1 != x:
        return v1
    elif v1 == x and v2 == x:
        return 2 * x_value[x_value[0]]
    else:
        return 0


def _get(rpn, x):      # 仅利用栈对逆波兰式解析,并直接求导
    stack = []
    for item in rpn:
        if item not in ["+", "-"] and item == x:
            stack.append("1")
        elif item not in ["+", "-"] and item != x:
            stack.append("0")
        else:
            b = stack.pop()
            a = stack.pop()
            tmp = "(" + a + " " + item + " " + b + ")"      # 组成算式
            stack.append(tmp)
    print(eval(stack[0]) % (10**9 + 7))


n, m = map(int, input().split())    # n,自变量的个数; m,要求解的偏导数的个数
rpn = input().split()       # 逆波兰式
rpn_len = len(rpn)
for i in range(m):
    dx_value = list(map(int, input().split()))      # 第1个整数是要求偏导数的自变量的编号；随后的整数是要求算的点的坐标
    if rpn_len == 1:    # 仅有一项
        print(1 if rpn[0] == "x" + str(dx_value[0]) else 0)
    elif rpn_len == 3:      # 仅有两项 运算符可能为 + - *
        if rpn[-1] == "+":
            r = d_add(rpn[0], rpn[1], "x" + str(dx_value[0]))
        elif rpn[-1] == "-":
            r = d_sub(rpn[0], rpn[1], "x" + str(dx_value[0]))
        else:
            r = d_mas(rpn[0], rpn[1], dx_value)
        print(int(r) % (10 ** 9 + 7))   # 按格式输出，对应的偏导数对10**9 +7取模的结果
    elif rpn_len > 3 and "*" not in rpn:    # 仅包含 + - 的情况
        _get(rpn, "x" + str(dx_value[0]))
    else:   # 乘法
        pass
