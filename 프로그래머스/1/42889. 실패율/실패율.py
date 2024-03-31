def solution(N, stages):
    player = len(stages)
    fail = {}
    
    for i in range(1, N+1):
        if player != 0:
            fail[i] = stages.count(i) / player
            player -= stages.count(i)
        else:
            fail[i] = 0
    answer = sorted(fail, key=lambda x: fail[x], reverse=True)

    return answer