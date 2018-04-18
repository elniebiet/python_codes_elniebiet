
f = 0
print(f)

f = 'abc'
print(f)

print('my name is michael ' + str(24))
#global and local variables
f = 0
print(f)

def someFunction():
    global f
    f = "def"
    print(f)
someFunction()          
#del f
print(f)
#mu;tiple assignments/initialisation
a = b = c = 1;
b = 5;
print('b is now: ', b)
a, b, c = 4, 5, 6
print('a is ',a,', b is ', b, ', and c is ',c)