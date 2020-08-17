# Code your solution here
def get_bool():
    x = (input())
    if x == 'true':
        return("SHUTDOWN")
    elif x == 'false':
        return("SHUTDOWN ABORTED")
    else:
        return("Not a boolean")

print(get_bool())
