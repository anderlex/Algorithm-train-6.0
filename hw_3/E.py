"""
1+(22*2 - 3)
1 22 2 * 3 - +

1+а+1
1 а + 1 +

1 1+2
1 1 2 +
"""

def solve(s):
    current_number = '' 
    arr = []
    ### Парсим в список без пробелов
    for sym in s:
        if sym.isdigit():
            current_number += sym
        elif sym.isalpha():
            return "WRONG"
        else:
            if current_number:
                arr.append(current_number)
                current_number = ""
            if sym != ' ':
                arr.append(sym)
    if current_number:
        arr.append(current_number)

    ### Парсим в ОНП
    priorities = {'*': 1, '+': 0, '-': 0}
    pol = []
    stack = []
    for sym in arr:
        if sym.isdigit():
            pol.append(sym)
        elif sym in "+-*":
            while stack and stack[-1] != '(' and priorities[stack[-1]] >= priorities[sym]:
                pol.append(stack.pop())
            stack.append(sym)
        elif sym == '(':
            stack.append(sym)
        elif sym == ')':
            while stack and stack[-1] != '(':
                pol.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            else: return "WRONG"

    while stack:
        if stack[-1] == '(':
            return "WRONG"
        pol.append(stack.pop())

    ### Вычисление
    nums = []
    for sym in pol:
        if sym.isdigit():
            nums.append(int(sym))
        else:
            if len(nums) < 2:
                return "WRONG"
            if sym == '+':
                res = nums[-1] + nums[-2]
                nums.pop()
                nums.pop()
                nums.append(res)
            elif sym == '*':
                res = nums[-1] * nums[-2]
                nums.pop()
                nums.pop()
                nums.append(res)
            elif sym == '-':
                res = nums[-2] - nums[-1]
                nums.pop()
                nums.pop()
                nums.append(res)
    
    return "WRONG" if len(nums) > 1 else nums[-1]

s = input()
print(solve(s))