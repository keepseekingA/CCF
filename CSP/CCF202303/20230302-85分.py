if __name__ == "__main__":
    tli = []    # 每个区序的耗时
    cli = []    # 每个区域缩短1天所需投入资源的基数
    tcdic = {}   # 用时t天，缩短一天所需的资源基数
    n, m, k = map(int, input().split())     # 区域块数，资源总数，每块区域最少开垦天数
    for i in range(n):
        t, c = map(int, input().split())
        tli.append(t)
        cli.append(c)
        if t not in tcdic:
            tcdic.update({t: 0})
        tcdic[t] += c
    total = max(tli)    # 最长用时
    csum = sum(cli)     # 全部区域缩短一天所需资源数
    keys = sorted(tcdic.keys())     # 用时类别
    while m >= 0 and total > k:     # 从大到小依次遍历，叠加耗费的资源
        now = keys.pop()
        if keys:
            nex = keys.pop()
            tcdic[nex] += tcdic[now]
        else:
            nex = now - 1
            tcdic[nex] = csum
        m = m - tcdic[now] * (now - nex)    # 从now到next花费代价后剩下的资源
        total = now
        keys.append(nex)
    print(total)
