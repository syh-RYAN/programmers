def solution(n, words):
    used = set()
    
    for i in range(len(words)):
        a = (i % n) +1
        b = (i // n ) +1
        
        if 1 < len(words[i]) and words[i] not in used :
            if i==0:
                used.add(words[i])
            elif words[i-1][-1] == words[i][0]:
                used.add(words[i])
            else:
                return[a,b]
            
        else:
            return[a,b]
    return[0,0]