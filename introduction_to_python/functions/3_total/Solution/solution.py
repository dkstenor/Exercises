# Code your solution here
def sum_data(lst):
    total = 0
    total = [total + num for num in lst]
    #for num in lst:
    #    total = total + num
    return total

my_lst = [1, 2, 3, 4, 5]
result = sum_data(my_lst)
print(result)