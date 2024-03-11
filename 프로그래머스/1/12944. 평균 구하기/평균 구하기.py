def solution(arr):
    if len(arr) == 0 :
        answer = 0
    else : 
        answer = sum(arr) / len(arr)
    return answer