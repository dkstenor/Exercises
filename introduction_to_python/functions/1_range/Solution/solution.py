# Code your solution here
def func_call():
    number = int(input())
    if number <= 100:
        return "GREATNESS"
    else:
        return "OOPS"

result = func_call()
print(result)