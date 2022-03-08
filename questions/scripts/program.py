def isValid(s):
    # write your code here
    stack = ['N']
    m = {')':'(',']':'[','}':'{'}
    for i in s:
        if i in m.keys():
            if stack.pop() != m[i]:
                return False
        else:
            stack.append(i)
            
    return len(stack) == 1
    