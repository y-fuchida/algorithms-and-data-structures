
N, D = map(int, input().split())
T_list = list(map(int, input().split()))

answer = -1
for i, t in enumerate(T_list):
    if i + 1 != len(T_list):
        if T_list[i + 1] - t <= D:
            answer = T_list[i + 1]
            break

print(answer)
