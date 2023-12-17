if __name__ == '__main__':
    n, m = map(int, input().split())
    n_li = [[int(j) for j in input().split()] for i in range(n)]
    store = []
    for i in range(n):
        s = n_li[i]     # 当前仓库
        s_store = []
        store_index = []
        compare_res = []    # 比较结果
        for item in n_li:   # item: 遍历的每一个仓库
            compare_res = [j > k for j, k in zip(item, s)]
            if False not in compare_res:
                s_store.append(item)
                store_index.append(n_li.index(item))
        if len(store_index) == 0:
            store.append(0)
            continue
        store.append(min(store_index)+1)
    # print(*store, sep="\n")
    for item in store:
        print(item)
