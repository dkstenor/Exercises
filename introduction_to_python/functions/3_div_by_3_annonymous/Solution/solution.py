# Code your solution here
def div_by_3(*args):
    new_list = list(filter(lambda x: x % 3 == 0, args))
    return new_list

my_list = div_by_3(1, 3, 9, 12)
print(my_list)