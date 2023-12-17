# def _dot(n, A, B):
#     for i in range(n):
#         for item in B[i]:
#             item *= A[i]
#             print("item:",item)
#         print("B的第{}行:".format(i),B[i])
#     return B


def _dot(n, _a, _b):
    for i in range(n):
        for j in range(len(_b[i])):
            _b[i][j] *= _a[i]
    return _b


def _cro(_a, _b):     # A的行数决定了C的行数， B的列数决定了C的列数
    _c = []
    for i in range(len(_a)):
        t1 = []
        for j in range(len(_b[0])):
            t2 = 0
            for k in range(len(_b)):
                t2 += _a[i][k] * _b[k][j]
            t1.append(t2)
        _c.append(t1)
    return _c


def main():
    n, d = map(int, input().split())
    matrix = {}
    matrix_key = ["Q", "K", "V"]
    for i in range(n * 3):  # 生成Q，K，V矩阵
        site = int(i / n)
        line = list(map(int, input().split()))
        if matrix_key[site] not in matrix.keys():
            matrix[matrix_key[site]] = []
        matrix[matrix_key[site]].append(line)
    W = list(map(int, input().split()))
    # 算KT
    KT = []
    for i in range(d):
        KT.append([matrix["K"][j][i] for j in range(n)])

    res1 = _cro(KT, matrix["V"])
    res2 = _cro(matrix["Q"], res1)
    res3 = _dot(n, W, res2)
    # res1 = _cro(matrix["Q"], KT)
    # res2 = _dot(n, W, res1)
    # res3 = _cro(res2, matrix["V"])
    for item in res3:
        print(*item)
        # st = ""
        # for it in item:
        #     st += "{} ".format(it)
        # s = st[:-1]
        # print(s)


if __name__ == "__main__":
    main()
