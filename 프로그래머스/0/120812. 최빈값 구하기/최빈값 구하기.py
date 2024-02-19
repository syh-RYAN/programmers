def solution(array):
    a = set(array)
    
    max_count = 0

    for i in a :
        count = array.count(i)
        if max_count < count :
            max_count = count
            answer = i
        elif max_count == count :
            answer = -1
    return answer