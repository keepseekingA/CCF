def decompose(num):   # 将整数num用因子形式表示 (因子，幂)
    ans = []
    i = 2
    while i * i <= num:   # 检查2-sqrt(n)
        tmp = 0
        while num % i == 0:   # 素数筛选算法, 筛掉i的倍数，每筛一次，i的幂次+1
            tmp += 1
            num //= i
        if tmp > 0:
            ans.append((i, tmp))
        i += 1
    if num > 1:   # 大于sqrt(n)的素因子最多只有1个
        ans.append((num, 1))
    return ans


if __name__ == "__main__":
    q = int(input())    # 查询个数
    for i in range(q):
        mlc = 1     # 乘积结果
        n, k = map(int, input().split())    # n:整数 k:阈值
        num_primes = decompose(n)    # 求n以内的所有素数因子，并用因子形式表示
        for item in num_primes:
            if item[1] >= k:
                mlc *= item[0]**item[1]
        print(mlc)
