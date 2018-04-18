def func():
    print("i am a function")
func()
print(func())
print(func)

def func2(arg1, arg2):
    print(arg1,'  ',arg2)

func2(2,3)

def cube(x):
    print(x*x*x)
cube(10)

def pow(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result
print(pow(8,2))
print(pow(2, 4))

def var_args(*args):
    result = 0
    for x in args:
        result = result + x
    return result
print(var_args(1,2,3,4))