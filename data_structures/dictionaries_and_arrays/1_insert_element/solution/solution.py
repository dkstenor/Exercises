# Write your solution here
import array

def insert_element(array_num, int_pos, int_val):
    arr = array.array('i', [int_val])
    return array_num[:int_pos] + arr + array_num[int_pos:]

x = array.array('i', [1, 2, 3])
print(insert_element(x, 1, 4))