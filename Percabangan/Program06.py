num1 = 10
num2 = 14
num3 = 12

if(num1 >= num2) and (num1 >= num3):
    terbesar = num1
elif(num2 >=num1) and (num2 >= num3):
    terbesar = num2
else:
    terbesar = num3

print('nilai terbesar : ', terbesar)