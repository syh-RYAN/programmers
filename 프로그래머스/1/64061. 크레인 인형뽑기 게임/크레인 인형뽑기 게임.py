def solution(board, moves):
    answer = 0
    basket = []
    n = len(board)
    column_board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            column_board[j][i] = board[i][j]
    
    for move in moves:
        move -= 1  

        for i in range(n):
            if column_board[move][i] != 0:
                doll = column_board[move][i]
                column_board[move][i] = 0  
                
                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2  
                else:
                    basket.append(doll)
                break 
            
    return answer