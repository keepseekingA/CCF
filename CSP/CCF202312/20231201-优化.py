if __name__ == '__main__':
    n, m = map(int, input().split())
    stores = [[int(j) for j in input().split()] for i in range(n)]    # 每个仓库编码列表,O(n*m)
    stores_index = []    # 编码和大于的仓库i的仓库下标
    stores_sum = []     # 每个仓库的编码和
    ans_index = []      # 第二维列表的仓库每个编码都大于对应下标的仓库编码
    for item in stores:     # 计算编码和,连sum所需时间复杂度O(n*m)
        stores_sum.append(sum(item))
    for i in range(n):      # 计算编码和大于的仓库i的仓库下标,O(n*n)
        _index = []
        for j in range(n):
            if i != j and stores_sum[j] >= stores_sum[i]:
                _index.append(j)
        stores_index.append(_index)
    for i in range(n):      # 找出全部编码都大于的仓库,O(k*n*m)
        ans = []
        # if len(stores_index[i]) == 0:     bug
        #     ans_index.append([-1])
        #     continue
        for k in stores_index[i]:
            tmp = 0
            for j in range(m):
                if stores[k][j] <= stores[i][j]:
                    break
                tmp += 1
            if tmp == m:
                ans.append(k)
        if len(ans) == 0:
            ans.append(-1)
        ans_index.append(ans)
    for ans in ans_index:       # 格式化输出 连min算 O(n)
        print(min(ans) + 1)
