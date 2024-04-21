def solution(s):
    answer = []
    s_list = s[2:-2].split('},{')
    sorted_s = sorted(s_list, key=lambda x: len(x))
    for i in sorted_s:
        s_split = i.split(',')
        answer.append(list(set(s_split)-set(answer))[0])
    
    
    return [int(i) for i in answer]