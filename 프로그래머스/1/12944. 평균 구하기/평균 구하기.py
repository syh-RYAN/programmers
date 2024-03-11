def solution(arr):
    a = 0
    for i in arr:
        a += i
    answer = a / len(arr)
    return answer