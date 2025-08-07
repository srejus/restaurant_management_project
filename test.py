def add_nums(a,b):
    return a+b


def multi(a,b):
    return a*b


def divide_2_nums(a,b):
    try:
        return a/b
    except:
        return None


from .t1 import sayHello

def say():
    name = "ram"
    res = sayHello(name)
    return res