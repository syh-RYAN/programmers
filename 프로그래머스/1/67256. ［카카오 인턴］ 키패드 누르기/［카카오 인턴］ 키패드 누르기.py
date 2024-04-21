def solution(numbers, hand):
    
    position = {'1':{'2':1, '5':2, '8':3, '0':4},
                '2':{'2':0, '5':1, '8':2, '0':3},
                '3':{'2':1, '5':2, '8':3, '0':4},
                '4':{'2':2, '5':1, '8':2, '0':3},
                '5':{'2':1, '5':0, '8':1, '0':2},
                '6':{'2':2, '5':1, '8':2, '0':3},
                '7':{'2':3, '5':2, '8':1, '0':2},
                '8':{'2':2, '5':1, '8':0, '0':1},
                '9':{'2':3, '5':2, '8':1, '0':2},
                '0':{'2':3, '5':2, '8':1, '0':0},
                '*':{'2':4, '5':3, '8':2, '0':1},
                '#':{'2':4, '5':3, '8':2, '0':1}
               }
            
    answer = ''
    right_hand = '#'
    left_hand = '*'
    for i in numbers :
        if i in [1,4,7]:
            left_hand = str(i)
            answer += 'L'
        elif i in [3,6,9]:
            right_hand = str(i)
            answer += 'R'
        else:
            if position[right_hand][str(i)] > position[left_hand][str(i)]:
                left_hand = str(i)
                answer += 'L'
            elif position[right_hand][str(i)] < position[left_hand][str(i)]:
                right_hand = str(i)
                answer += 'R'
            else :
                if hand =='right':
                    right_hand = str(i)
                    answer += 'R'
                else :
                    left_hand = str(i)
                    answer += 'L'
    return answer