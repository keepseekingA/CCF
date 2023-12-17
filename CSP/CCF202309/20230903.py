def d_add(v1, v2, x):
    return 1 if v1 == x or v2 == x else 0


def d_sub(v1, v2, x):
    if v1 == x:
        return 1
    elif v2 == x:
        return -1
    else:
        return 0


def d_mas(v1, v2, x_value):
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
            tmp = "(" + a + " " + item + " " + b + ")"
            stack.append(tmp)
    print(eval(stack[0]) % (10**9 +7))


n, m = map(int, input().split())
rpn = input().split()
rpn_len = len(rpn)
for i in range(m):
    dx_value = list(map(int, input().split()))
    if rpn_len == 1:
        print(1 if rpn[0] == "x" + str(dx_value[0]) else 0)
    elif rpn_len == 3:
        if rpn[-1] == "+":
            r = d_add(rpn[0], rpn[1], "x" + str(dx_value[0]))
        elif rpn[-1] == "-":
            r = d_sub(rpn[0], rpn[1], "x" + str(dx_value[0]))
        else:
            r = d_mas(rpn[0], rpn[1], dx_value)
        print(int(r) % (10 ** 9 + 7))
    elif rpn_len > 3 and "*" not in rpn:
        _get(rpn, "x" + str(dx_value[0]))
    else:   # 乘法
        pass
