# coding=utf-8
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A

# BubbleSort(A)
# 1 for i = 0 to A.length-1
# 2     for j = A.length-1 downto i+1
# 3         if A[j] < A[j-1]
# 4             swap A[j] and A[j-1]

# input
n = int(input())
a = list(map(int, input().split()))

# process
swap = 0
# 未ソートの部分を先頭を指すループ変数
for i in range(n-1):
    # 配列の末尾から要素を比較して、ソート済みまで並び替える
    for j in reversed(range(i+1, n)):
        # 今の値より左隣が大きかったらswap
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            swap += 1

print(*a)
print(swap)



