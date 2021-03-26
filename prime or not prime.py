ans = ''
un = int(input('What is your number ?'))
for d in range (2, un):
    if un %d== 0:
        ans = 'not prime'
        break


if ans == '':
    ans = 'prime'

print(ans)