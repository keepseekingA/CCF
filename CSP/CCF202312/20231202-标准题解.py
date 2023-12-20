def get_primes(num):     # 求n以内的所有素数
    prime_li = [True] * (num + 1)   # i * j = num
    for i in range(2, num//2 +1):   # i
        for j in range(2, num//i +1):   # j
            prime_li[j * i] = False
    return prime_li


def decompose(n):
    ans = []
    i = 2
    while i * i <= n:
        tmp = 0
        while n % i == 0:
            tmp += 1
            n //= i
        if tmp > 0:
            ans.append((i, tmp))
        i += 1
    if n > 1:
        ans.append((n, 1))
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
