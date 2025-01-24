# ビット全探索
def bit_explore(items):
    n = len(items)
    all_subsets = []
    
    # 2^n 通りの組み合わせをループ
    for bit in range(1 << n):  # 1 << n は 2^n を意味する
        subset = []
        for i in range(n):
            # bit の i 番目が 1 なら items[i] を含める
            if bit & (1 << i):  # (1 << i) は 2^i を意味する
                subset.append(items[i])
        all_subsets.append(subset)
    
    return all_subsets

# 使用例
items = ['a', 'b', 'c']
subsets = bit_explore(items)
for subset in subsets:
    print(subset)
