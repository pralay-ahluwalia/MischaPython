#sn = int (input('What is your start number ? '))
en = int (input('What is your number ? '))
cn = 0
for d in range (1,en + 1):
    lastnum = 0
    ans = ''
    z = 0

    cn = en - d
    for i in range(2,cn):
         if cn % i  == 0:
            ans= 'not prime'


    if ans == '':
        ans = 'prime'
        break
        lastnum=d

print (lastnum)

