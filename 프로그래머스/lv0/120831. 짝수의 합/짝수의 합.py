def solution(n):
    list = []
    for i in range(0,n+1) :
        if i % 2 == 0 :
            list.append(i)
        answer = sum(list)
    return answer