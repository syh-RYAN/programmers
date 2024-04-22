def solution(box, n):
    answer = int((box[0]//n) * (box[1]//n) * (box[2]//n))
    return answer