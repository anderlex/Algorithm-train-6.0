A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A == 0:
    print(1, C + 1)
elif B == 0:
    print(1, D + 1)
elif C == 0:
    print(A + 1, 1)
elif D == 0:
    print(B + 1, 1)
else:
    x1 = 1 + max(C, D) + 1
    x2 = max(A, B) + 1 + 1
    x3 = A + C + 2
    x4 = B + D + 2
    ans = min(x1, x2, x3, x4)
    if ans == x1:
        print(1, max(C, D) + 1)
    elif ans == x2:
        print(max(A, B) + 1, 1)
    elif ans == x3:
        print(A + 1, C + 1)
    else:
        print(B + 1, D + 1)