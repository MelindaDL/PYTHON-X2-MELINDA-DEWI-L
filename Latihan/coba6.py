kalimat = "Nama saya Umar"

print(kalimat)      # print string lengkap
print(kalimat[0])   # print karakter pertama
print(kalimat[-1])  # print karakter terakhir
print(kalimat[4:7]) # print dari indeks 4 - 6
print(kalimat[:4])  # print dari indeks 0 - 3


a = [5,10,15,20,25,30,35,40]
 
# a[2] = 15
print("a[2] = ", a[2])
 
# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])
 
# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:]) 
 



# set integer 
my_set = {1,2,3} 
print(my_set) 
 
# set dengan menggunakan fungsi set() 
my_set = set([1,2,3]) 
print(my_set) 
 
# set data campuran 
my_set = {1, 2.0, "Python", (3,4,5)} 
print(my_set) 
 
# bila kita mengisi duplikasi, set akan menghilangkan salah satu 
# output: {1,2,3} 
my_set = {1,2,2,3,3,3} 
print(my_set) 
 
 