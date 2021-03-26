i = int (input ('Which prime number do u want ?'))
sn = int (input('What is your start number ? '))
en = int (input('What is your end number ? '))
z = 0
counter = 0
for d in range (sn ,en+1):
    ans = ''
    for i in range(2,d):
        if d % i  == 0:
            ans= 'not prime'
            break
    if ans == '':
        ans = 'prime'
        z = z + 1
if i>z :
    print ( 'The prime number you want is bigger than the prime numbers between ' + str(sn) + ' and '+ str (en) + '.')
print (z)



