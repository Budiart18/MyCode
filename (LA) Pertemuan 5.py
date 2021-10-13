#Menampilkan Deret Bilangan
deret = int(input("Banyak Data = "))
for i in range (deret):
    print(i)

#Menampilkan Deret Bilangan Genap
n = int(input("Masukkan Biangan n = "))
x = 2
while x <= n:
    print(x, end=" ")
    x = x + 2

#Menampilkan Bilangan 1-20
angka = 1
while angka<=15:
    print("Bilangan ke",angka)
    angka=angka+1
print("Terima Kasih")

#Menampilkan Bilangan 10-1
bil = 10
while bil > 0:
    print(bil)
    bil = bil - 1
print("Terima Kasih")

#Menentukan Bilangan Prima atau tidak
bilangan = int(input("Masukkan Bilangan = "))
if bilangan > 1:
    for faktor in range(2,bilangan):
        if (bilangan % faktor == 0):
            prima = "BUKAN PRIMA"
            break
        else:
            prima = "PRIMA"
    print(bilangan, "adalah bilangan", prima)
elif bilangan == 2:
    print("2 adalah bilangan PRIMA")
else:
    print(bilangan, "bilangan harus > 1")

#penggunaan continue pada while
bil = 0
pilihan = 'y'
while (pilihan != 'n'):
    bil = int(input("Masukkan bilangan dibawah 50: "))
    if (bil > 50):
        print("Bilangan melebihi angka 50, Silahkan diulangi.")
        continue
    print("Pangkat dua dari bilangan ini adalah: ",bil*bil)
    pilihan = input("Apakah Anda ingin mengulang kembali (y/n)? ")


#Program Menggunakan Nested While
#Untuk mencetak bilangan prima antara 1 sampai 50
i = 2
while(i < 4):
    j = 2
    while(j <= (i/j)):
        if not(i%j):
            break
        j = j + 1
    if (j > i/j) :
        print (i, "adalah Bilangan Prima")
    i = i + 1
print("Terima Kasih")

#Latihan Ayam
bil = 0
pilihan = 'y'
while (pilihan != 'n'):
    bil = int(input("Masukkan bilangan (1-100) = "))
    if (bil < 1) or (bil > 100):
        print("Bilangan harus antara 1-100, Silahkan diulangi.")
        continue
    print("Tek kotek kotek kotek, anak ayam turun berkotek")
    while (bil > 0):
        bil2 = bil - 1
        if (bil2 == 0):
            bil2 = "induknya"
        print("anak ayam turunlah", bil, "mati satu tinggallah", bil2)
        bil = bil - 1
    pilihan = input("Apakah Anda ingin mengulang kembali (y/n)? ")