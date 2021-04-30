a = 4
if a % 3 !=0:
    print (a, 'habis dibagi 3')
if a // 3 !=0:
    print(a,"lebih kecil dari 3")

a = 5
b = 7
c = 9
if a > b:
    if a < c:
        print('1', end='' , sep='')
    elif c < b:
        print('2', end='' , sep='')
    elif b > a:
        print('3', end='' , sep='')
    else :
        print('4', end='' , sep='')

elif c > b:
    if a > c:
        print('5', end='' , sep='')
    elif c > b:
        print('6', end='' , sep='')
    elif b < a:
        print('7', end='' , sep='')
    else :
        print('8', end='' , sep='')
else:
    print('9', end='' , sep='')

print('10') 