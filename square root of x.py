cub =0
num = int(input('What is your number ?'))
afdezi = int(input('How many places after the decimal do you want?'))
start = 0
end = num
mid = (start + end) / 2
for div in range (1,100):
    mid = (start + end) / 2
    if num > mid * mid:
        start = mid
    else:
        end = mid
t = (end+start)/2
a = start * start
b = t *t
c = end * end
cl1 = num - a
cl3 = c - num
if b > num :
    cl2 = b - num
else:
    cl2 = num - b
if cl1> cl2:
    if cl3 > cl2:
        print('The square root of '+str (num)+' is close too '+str(mid))
        print('If you multiply '+str(mid )+' and '+str(mid)+' it equals '+str(b))
        cub = mid
    else:
        print('The square root of '+str (num)+' is close too '+str(end))
        print('If you multiply ' + str(end) + ' and ' + str(end) + ' it equals ' + str(c))
        cub = end
else:
    if cl1 < cl3:
        print('The square root of '+str (num)+' is close too '+str(start))
        print('If you multiply ' + str(start) + ' and ' + str(start) + ' it equals ' + str(a))
        cub = start
print(cub)