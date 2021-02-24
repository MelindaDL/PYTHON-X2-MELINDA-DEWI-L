num = int(input('bilangan : '))

faktorial = 1

if num < 0:
    print('maaf, faktorial tidak bisa untuk bilangan negatif')
elif num == 0:
    print('faktorial dari 0 adalah 1')
else:
    for i in range(1,num+1):
        faktorial = faktorial*i
    print('faktorial dari',num,'adalah',faktorial)
