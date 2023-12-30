if __name__ == "__main__":
    tli = []    # 每个区序的耗时
    cli = []    # 每个区域缩短1天所需投入资源的基数
    n, m, k = map(int, input().split())     # 区域块数，资源总数，每块区域最少开垦天数
    for i in range(n):
        t, c = map(int, input().split())
        tli.append(t)
        cli.append(c)
    total = max(tli)  # 总耗时
    totalc = sum(cli)   # 降低一天所需的最少资源
    while m > 0 and total > k:
        for i in range(n):
            if tli[i] == total:
                tli[i] -= 1
                m -= cli[i]
        if m < 0:
            break
        total = max(tli)
    print(total)     # 最少耗时
