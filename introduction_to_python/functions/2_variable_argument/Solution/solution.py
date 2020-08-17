# Code your solution here
def my_func(*args):
    my_str = " "
    for x in args:
        my_str += x
    return my_str

result = my_func("One", "Two", "Three")
print(result)