lower = 900
upper = 1000

print('bilangan prima antara',lower,'dan',upper,'adalah')

for num in range (lower,upper+1):
    if num > 1:
        for i in range (2,num) :
            if (num %2) ==0:
                break
        else:
            print (num)