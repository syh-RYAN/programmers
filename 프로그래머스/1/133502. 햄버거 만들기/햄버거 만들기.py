def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        if i ==1 and stack[-3:] == [1,2,3]:
            del stack[-3:]
            answer +=1
        else:
            stack.append(i)
    return answer