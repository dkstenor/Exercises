# Code your solution here
def count_even(*args):
    evens = 0
    for i in args:
        if i % 2 == 0:
            evens +=1
    return evens
    
num=count_even(1, 2, 3, 4)
print(num)