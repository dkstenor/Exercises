# Write your solution here
def occurances(array_num, element):
    count = 0
    for el in array_num:
        if el == element:
            count +=1
    return count