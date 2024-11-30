n = int(input())
value_stack = []
prefix_stack = [0]

for i in range(n):
    cur = input()
    if cur[0] == '+':
        new_val = int(cur[1:])
        value_stack.append(new_val)
        prefix_stack.append(new_val + prefix_stack[-1])
    elif cur == '-':
        print(value_stack.pop())
        prefix_stack.pop()
    elif cur[0] == '?':
        k = int(cur[1:])
        m = len(prefix_stack)
        print(prefix_stack[-1] - prefix_stack[-1 - k])