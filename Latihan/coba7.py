# contoh penggunaan statement break
for letter in "Programming":
    if letter == "g":
        continue
    print("Huruf sekarang:", letter)
print("Good bye")


count = 0
while (count < 5):
    print(count, "kurang dari 5")
    count = count + 1
else:
    print(count, "tidak kurang dari 5")
