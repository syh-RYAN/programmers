def solution(my_string):
    a = ['a','e','i','o','u']
    for i in a:
        my_string = my_string.replace(i, '')
    return my_string