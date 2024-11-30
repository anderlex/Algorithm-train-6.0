n = int(input())
w = list(input())
s = input()

stack = []
for b in s:
    if b in "([":
        stack.append(b)
    elif b == ')':
        if stack and stack[-1] == '(':
            stack.pop()
    elif b == ']':
        if stack and stack[-1] == '[':
            stack.pop()

cur = ''

while len(s) < n - len(stack):
    if stack:
        if stack[-1] == '(':
            if w.index(')') == 0:
                s += ')'
                stack.pop()
            elif w.index('(') == 0:
                s += '('
                stack.append('(')
            elif w.index('[') == 0:
                s += '['
                stack.append('[')
            else:
                if w[1] == ')':
                    s += ')'
                    stack.pop()
                else:
                    s += w[1]
                    stack.append(w[1])
        elif stack[-1] == '[':
            if w.index(']') == 0:
                s += ']'
                stack.pop()
            elif w.index('(') == 0:
                s += '('
                stack.append('(')
            elif w.index('[') == 0:
                s += '['
                stack.append('[')
            else:
                if w[1] == ']':
                    s += ']'
                    stack.pop()
                else:
                    s += w[1]
                    stack.append(w[1])
    else:
        if w.index('(') < w.index('['):
            s += '('
            stack.append('(')
        else:
            s += '['
            stack.append('[')

while stack:
    b = stack.pop()
    if b == '(':
        s += ')'
    else: s += ']'

print(s)