sn = int (input('What is your start number ? '))
en = int (input('What is your end number ? '))
z = 0
for d in range (sn ,en+1):

    ans = ''

    for i in range(2,d):
        if d % i  == 0:
            ans= 'not prime'
            break
    if ans == '':
        z = z +1
        ans = ' prime'

print(z)
print ('There are '+ str (z) + ' prime numbers'+ ' between '+ str(sn) + ' and ' + str(en))



