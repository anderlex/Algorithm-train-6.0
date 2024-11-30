N = int(input())
a, b = map(int, input().split())

if a > b: a, b = b, a

rovers = []
for i in range(N):
    road, t = map(int, input().split())
    rovers.append((t, road, i))
rovers.sort()

c, d = 0, 0
for i in range(4):
    if not (i == a - 1 or i == b - 1):
        c = i + 1
d = 10 - a - b - c
if c > d: c, d = d, c
    
sides = [[] for i in range(4)]
answer = [0 for i in range(N)]

for t in range(1, 202):
    for rover in rovers:
        if rover[0] == t:
            sides[rover[1] - 1].append(rover[2])
    if sides[a - 1]:
        if sides[b - 1]:
            if b - a == 2:
                answer[sides[b - 1].pop(0)] = t
                answer[sides[a - 1].pop(0)] = t
            elif b - a == 1:
                answer[sides[a - 1].pop(0)] = t
            else:
                answer[sides[b - 1].pop(0)] = t
        else:
            answer[sides[a - 1].pop(0)] = t
    elif sides[b - 1]:
        answer[sides[b - 1].pop(0)] = t
    elif sides[c - 1]:
        if sides[d - 1]:
            if d - c == 2:
                answer[sides[d - 1].pop(0)] = t
                answer[sides[c - 1].pop(0)] = t
            elif d - c == 1:
                answer[sides[c - 1].pop(0)] = t
            else:
                answer[sides[d - 1].pop(0)] = t
        else:
            answer[sides[c - 1].pop(0)] = t
    elif sides[d - 1]:
        answer[sides[d - 1].pop(0)] = t 

for a in answer:
    print(a)