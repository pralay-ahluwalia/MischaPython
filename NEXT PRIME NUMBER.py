sn = int (input('What is your number ? '))
for d in range (sn + 1 ,sn + 1000000):
    ans = ''
    for i in range(2,d):
        if d % i  == 0:
            ans= 'not prime'
            break
    if ans == '':
        ans = 'prime'
        break
print ('The next prime number after '+ str(sn) +' is '+ str(d))