def solution(k, dungeons):
    answer = 0  
    stack = []  

    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:  # 현재 체력으로 던전에 입장 가능한 경우
            # [남은 체력, 던전 인덱스] 형태로 stack에 추가
            stack.append([k-dungeons[i][1], i])

    while stack:  # stack이 비어있지 않은 동안 반복
        order = stack.pop()  # 현재까지 방문한 던전 순서와 남은 체력
        value = order[0]  # 현재 남은 체력
        size = len(order)-1  # 현재까지 방문한 던전 수

        answer = max(answer, size)  # 최대 방문 던전 수 업데이트

        if size == len(dungeons):  # 모든 던전을 방문한 경우
            # 더 이상 탐색할 필요 없으므로 반복문 종료
            break

        for i in range(len(dungeons)):
            if i not in order[1:] and dungeons[i][0] <= value:
                # 아직 방문하지 않은 던전이며, 현재 체력으로 입장 가능한 경우
                temp = order[:]  # 이전 순서를 복사
                temp[0] -= dungeons[i][1]  # 새로 방문할 던전에서 소모되는 체력 차감
                temp.append(i)  # 새로 방문할 던전 인덱스 추가
                stack.append(temp)  # 새로운 순서를 stack에 추가

    return answer  # 최대 방문 가능한 던전 수 반환