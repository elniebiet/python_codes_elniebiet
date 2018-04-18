def dig_pow(n, p):
    number = str(n)
    n_digits = len(number)
    k = 0
    for num in range(n_digits):
        k = k + pow(int(number[num]),p+num)
    if(n != 0 and (k % n == 0)):
        
        return (k/n)
    else:
        return -1
print(dig_pow(695,2))