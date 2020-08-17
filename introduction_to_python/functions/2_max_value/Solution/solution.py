# Code your solution here
def max_val():
    x, y, z = input("Enter three integers:  ").split(' ')
    a = int(x)
    b = int(y)
    c = int(z)
    max_value = a
    if b > a:
        max_value = b
    if c > b:
        max_value = c
    return max_value


result = max_val()
print(result)
