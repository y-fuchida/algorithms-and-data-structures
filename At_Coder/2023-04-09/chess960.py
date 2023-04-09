
S = input()

b1 = S.find("B")
b2 = S.find("B", b1+1)

r1 = S.find("R")
r2 = S.find("R", r1+1)
k = S.find("K")

if (b2-b1) % 2 == 0:
    print("No")
elif not (r1 < k < r2):
    print("No")
else:
    print("Yes")


