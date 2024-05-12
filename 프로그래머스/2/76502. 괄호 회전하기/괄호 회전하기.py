def rotation(s):
    stack = []
    for i in s:
        if stack and stack[-1] == '[' and i == ']':
            del stack[-1]
        elif stack and stack[-1] == '{' and i == '}':
            del stack[-1]
        elif stack and stack[-1] == '(' and i ==')' :
            del stack[-1]
        else:
            stack.append(i)
    return stack == []
def solution(s):
    answer = 0
    for x in range(len(s)):
        if rotation(s[x:] + s[:x]):
            answer += 1
    return answer