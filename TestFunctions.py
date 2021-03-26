def CheckPrime(numtocheck,r):
    for i in range( 2, numtocheck ):
        if numtocheck % i == 0:
            r = 0
            return
    r = 1
    return;

n = int(input('Number Pls : '))
r = ''
CheckPrime(n, r)
if r == 1:
    print("prime")