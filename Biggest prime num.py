usernum = int (input('What is your number ?'))
for d in range (1 ,usernum):
    r = usernum - d
    ans = ''
    z = 0
    for i in range(2,r):
        if r % i  == 0:
            ans= 'not prime'
            break
    if ans == '':
        ans = 'prime'
        z = r
        break
print('The biggest prime number under ' + str ( usernum ) + ' is ' + str ( r) + '.' )
#test 123


