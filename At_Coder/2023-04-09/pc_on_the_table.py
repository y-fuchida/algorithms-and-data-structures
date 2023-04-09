
H, W = map(int, input().split())

S_list = [input() for _ in range(H)]

for _s in S_list:
    s = [c for c in _s]
    for i in range(W):
        if i + 1 != W and s[i] == "T" and s[i+1] == "T":
            s[i] = "P"
            s[i+1] = "C"
        print(s[i], end='')
    print()
