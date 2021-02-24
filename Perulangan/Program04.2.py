lower = 100
upper = 2000

for num in range (lower,upper+1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0 :
        digital = temp % 10
        sum += digital ** order
        temp //= 10

    if num == sum:
        print (num)