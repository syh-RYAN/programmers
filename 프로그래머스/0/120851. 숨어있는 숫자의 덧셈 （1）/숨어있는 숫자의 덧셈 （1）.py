def solution(my_string):
    a = ''.join(filter(str.isdigit,my_string))
    b = map(int, str(a))
    c = list(b)
    return sum(c)