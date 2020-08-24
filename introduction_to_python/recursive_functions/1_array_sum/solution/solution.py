# Write your solution here
def sum_array(num_list):
    if num_list == []:
        return 0
    else:
        return(num_list[0] + sum_array(num_list[1:]))

print(sum_array([1, 2, 3, 4, 5]))