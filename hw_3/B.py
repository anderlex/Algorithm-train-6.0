n = int(input())
p = list(map(int, input().split()))

result = [-1] * n
stack = [0]
for i in range(1, n):
    if p[i - 1] < p[i]:
        stack.append(i)
    else:
        while stack and p[stack[-1]] >  p[i]:
            result[stack[-1]] = i
            stack.pop()
        stack.append(i)

for res in result:
    print(res, end=' ')