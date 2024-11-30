def brack_sequence(s):
    stack = []
    for bracket in s:
        if bracket in "([{":
            stack.append(bracket)
        elif bracket == ')':
            if not stack or stack[-1] != '(':
                return "no"
            else:
                stack.pop()
        elif bracket == ']':
            if not stack or stack[-1] != '[':
                return "no"
            else:
                stack.pop()
        elif bracket == '}':
            if not stack or stack[-1] != '{':
                return "no"
            else:
                stack.pop()
    return "yes" if not stack else "no"

s = input()
        
print(brack_sequence(s))