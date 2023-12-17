def is_prime(num):      # 判断是否为素数
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True


def prime_item(num):      # 求素数因子：因子对应的指数
    # 求 2到sqrt(10**10)的素数因子
    prime_li = []
    prime_dic = {}
    for i in range(2, 100000):   # 因子
        if is_prime(i):
            prime_dic[i] = 0
            prime_li.append(i)
    # 求素数因子的指数
    for prime in prime_li:
        while num % prime == 0:
            prime_dic[prime] += 1
            num = num / prime
        if num == 1:
            break
    # 处理非因子的素数
    del_key = []
    for key in prime_dic.keys():
        if prime_dic[key] == 0:
            del_key.append(key)
    for key in del_key:
        del prime_dic[key]
    return prime_dic


if __name__ == "__main__":
    q = int(input())    # 查询个数
    for i in range(q):
        mlc = 1     # 乘积结果
        n, k = map(int, input().split())    # n:整数 k:阈值
        primes = prime_item(n)
        for item in primes.items():
            if item[1] >= k:
                mlc *= item[0]**item[1]
        print(mlc)
