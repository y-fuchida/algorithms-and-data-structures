# coding=utf-8
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A

# BubbleSort(A)
# 1 for i = 0 to A.length-1
# 2     for j = A.length-1 downto i+1
# 3         if A[j] < A[j-1]
# 4             swap A[j] and A[j-1]

# input
N = int(input())
arr = list(map(int, input().split()))

# process
# 未ソートの部分を先頭を指すループ変数
for idx in range(0, N-1):
    print(idx)
    # 配列の末尾から要素を比較して、ソート済みまで並び替える
    # for j in reversed(range(idx+1, len(arr))):
    #     print(j)
    # test