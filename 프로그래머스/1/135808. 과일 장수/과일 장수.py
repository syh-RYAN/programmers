def solution(k, m, score):
    score.sort(reverse=True)
    box = []
    answer = 0
    
    if len(score) < m :
        print(0)
    else :
        for i in range(0, len(score),m) :
            box = score[i:i+m]
            
            if len(box) < m :
                break
            answer += box[-1] * m
    return answer