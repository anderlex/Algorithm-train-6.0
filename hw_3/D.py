s = list(input().split())

nums = []
for sym in s:
    if sym.isdigit():
        nums.append(int(sym))
    else:
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
print(nums[-1])