cub = 0
num = int(input('What is your number ?'))
afdezi = int(input('How many places after the decimal do you want?'))
start = 0
end = num
mid = (start + end) / 2
for multi in range (1,100):
    mid = (start + end) /2
    if num > mid * mid * mid:
        start = mid
    else:
        end = mid
ergebnis=0
a = start * start * start
b = mid * mid * mid
c = end * end * end
cl1 = num - a
if b > num:
    cl2 = b - num
else:
    cl2 = num - b
cl3 = c - num

if cl1 > cl2:
    if cl3 > cl2:
        cub = mid
    else:
        cub = end
else:
    if cl1 < cl3:
        cub = start
    else:
        cub = end
text = cub
text = str(text)
split = text.split('.')
decimals = split[1]
lenght = len(decimals)
if afdezi>lenght:
    print('There are too less places')
    print('The cube root of ' + str(num) + ' is close too ' + str(cub))
    print(str(cub) + ' times ' + str(cub) + ' times ' + str(cub) + ' equals ' + str(cub*cub*cub))
if lenght > afdezi:
    decimals1 = int(decimals)
    z = decimals[afdezi-1]
    ä = int(z)
    ö = decimals[afdezi]
    #print(ä)
    #print(ö)
    if int(ö) < 4:
        ergebnis = split[0] + '.' + decimals[0:afdezi]
        print('The cube root of ' + str(num) + ' is close too ' + str(cub))
        print(str(cub) + ' times ' + str(cub) + ' times ' + str(cub) + ' equals ' + str(cub * cub * cub))
        print('If you round it too the ' + str(afdezi) + ' place it will become ' + str(ergebnis))
        decimals1 = int(decimals)
        z = decimals[afdezi - 1]
        ä = int(z)
        ö = decimals[afdezi]
    if int(ö) > 4:
        z = ä + 1
        ergebnis = split[0]+'.'+decimals[0:afdezi-1]+str(z)
        print('The cube root of ' + str(num) + ' is close too ' + str(cub))
        print(str(cub) + ' times ' + str(cub) + ' times ' + str(cub) + ' equals ' + str(cub * cub * cub))
        print('If you round it too the ' + str(afdezi) + ' place it will become ' + str(ergebnis))