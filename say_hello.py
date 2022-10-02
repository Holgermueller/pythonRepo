# def say_hi(name):
#     print('Hello ' + name)


# say_hi("Stu")
# say_hi('Lowell')

def count_substring(string, sub_string):
    return string.upper().count(sub_string.upper())


print(count_substring('abcdcdc', 'cdc'))
