# Code your solution here
def concat_args(*args):
    my_str = " "
    for x in args:
        my_str += x
    return my_str

result = concat_args()
print(result)
