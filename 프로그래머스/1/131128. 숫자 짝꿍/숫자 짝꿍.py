def solution(X, Y):
    answer = ''
    a = set(X) & set(Y)
    a = list(a)
    a.sort(reverse=True)
    
    for i in a:
        x = X.count(i)
        y = Y.count(i)
        answer += i * min(x, y)
    if not len(a): 
        answer = '-1'
    elif answer.count('0') == len(answer):
        answer = '0'
    return answer