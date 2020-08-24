# Write your solution here
def reverse(my_str):
    if my_str == '':
        return ''
    rev_str = my_str[-1] + reverse(my_str[0:-1])
    return(rev_str)
