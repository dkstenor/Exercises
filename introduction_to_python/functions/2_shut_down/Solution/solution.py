# Code your solution here
def shut_down():
    x = (input())
    if x == 'true':
        return("SHUTDOWN")
    elif x == 'false':
        return("SHUTDOWN ABORTED")
    else:
        return("Not a boolean")

print(shut_down())
