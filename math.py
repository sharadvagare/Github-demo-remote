# add implementation
def add(x,y):
    return x+y
#subtract implementation
def subtract(x,y):
    return x-y          # master
#multiply implementation
def multiply(x,y):
    return x*y          #bug456
#divide implementation
def divide(x,y):
    if y==0:            #master
        return divide_by_0_error
    else
        return x/y