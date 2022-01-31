# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_B

# SelectionSort(A)
# 1 for i = 0 to A.length-1
# 2     mini = i
# 3     for j = i to A.length-1
# 4         if A[j] < A[mini]
# 5             mini = j
# 6     swap A[i] and A[mini]

# Input
N = int(input())
A = list(map(int, input().split()))

# Process
swap = 0


# 未ソートの部分の先頭を表すループ変数で、
# 配列の先頭から末尾に向かって移動する
for i in range(N-1):
    # 各ループの処理でi番目からN-1番目までの要素で最小のものの位置
    mini = i
    # 未ソートの部分化から最小値の位置（mini）を探すためのループ変数
    for j in range(i, N):
        if A[j] < A[mini]:
            mini = j
    A[i], A[mini] = A[mini], A[i]
    if i != mini:
        swap += 1

print(*A)
print(swap)
