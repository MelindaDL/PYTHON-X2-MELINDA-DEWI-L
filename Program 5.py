tahun = int(input('masukkan tahun : '))

if (tahun % 4) == 0:
    if(tahun % 100) == 0:
        if(tahun % 400) == 0:
            print('{0} adalah tahun kabisat'.format(tahun))
        else:
            print('{0} bukan tahun kabisat'.format(tahun))
    else:
        print('{0} adalah tahun kabisat'.format(tahun))
else:
    print('{0} bukan tahun kabisat'.format(tahun))