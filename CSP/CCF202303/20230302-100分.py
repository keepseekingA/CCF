if __name__ == '__main__':
    tli = []  # 每个区序的耗时
    cli = []  # 每个区域缩短1天所需投入资源的基数
    tcosts = list()   # 用时t天，缩短一天所需的资源基数
    n, m, k = map(int, input().split())  # 区域块数，资源总数，每块区域最少开垦天数
    for i in range(n):      # 初始化tli、cli
        t, c = map(int, input().split())
        tli.append(t)
        cli.append(c)
    total = max(tli)
    tcosts = [0] * (total + 1)
    # 构造下标=时间，值=缩短一天所需的资源基数 的映射
    for i in range(n):
        t = tli[i]
        tcosts[t] += cli[i]
    # 检查有限资源内，最低降至多少天
    for i in range(max(tli), -1, -1):
        # print(i, "\t total:",total, "\t m:", m, "\t", tcosts[i])
        if total == k:
            break
        if m > tcosts[i]:
            m = m - tcosts[i]
            tcosts[i-1] += tcosts[i]
            total -= 1
        else:
            break
    print(total)
