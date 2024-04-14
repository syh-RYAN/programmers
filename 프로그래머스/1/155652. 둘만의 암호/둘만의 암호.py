def solution(s, skip, index):
    alpha = ''.join(char for char in 'abcdefghijklmnopqrstuvwxyz' if char not in set(skip))
    answer = ''

    for char in s:
        if char in alpha:
            char_index = alpha.index(char)
            new_index = (char_index + index) % len(alpha)
            answer += alpha[new_index]
        else:
            answer += char

    return answer