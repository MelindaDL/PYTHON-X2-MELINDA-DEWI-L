def segitiga(a,t) :
    luas = (a * t)/2
    return luas

print ("Mencari luas segitiga")
a = int(input('alas: '))
t = int(input('tinggi: '))

print('luas : ', segitiga(a,t))
