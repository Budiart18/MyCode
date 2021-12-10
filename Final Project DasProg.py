import pandas as pd

#Fungsi Login
def login():
    print("=" * 50)
    print("Halaman Login Kasir Ayam Digeprek")
    username = input("Masukan Username: ")
    password = input("Masukan Password: ")
    if username == "admin" and password == "adminpass":
        print("Login berhasil...\n\n")
        main_menu()
    else:
        print("Login gagal. Silahkan coba lagi...")
        login()
        
#Fungsi Main menu kasir
def main_menu():
    print("=" * 10, "MAIN MENU AYAM DIGEPREK", "=" * 10)
    print("Selamat Datang Di Ayam Digeprek")
    print("=" * 10, "Masukan Input Aplikasi", "=" * 10)
    print("1. Daftar Harga")
    print("2. Kasir")
    print("3. Exit Program") 
    # input pilihan
    pilihan = input("Pilih menu (1/2/3) = ")
    # pilihan menu
    if pilihan == "1":
        daftar_harga()
    elif pilihan == "2":
        kasir()
    else:
        print("Program Exit")
        exit()

#Fungsi Daftar harga     
def daftar_harga():
    print("DAFTAR HARGA AYAM DIGEPREK".center(70," "))
    print("="*70)
    print("NO. \t JENIS \t\t HARGA SATUAN")
    print("1. \t DADA \t\t Rp. 2500")
    print("2. \t PAHA \t\t Rp. 2000")
    print("3. \t SAYAP \t\t Rp. 1000")
    pertanyaan()
              
#Fungsi Kasir
def kasir():
    #Inisialisasi List
    list_kode = []
    list_jenis = []
    list_harga = []
    list_banyak = []
    list_jumlah = []
    #Berapa Banyak jenis order
    banyak_jenis = int(input("Masukkan Banyak Jenis = "))
    #Perulangan Inputan
    jumlah_bayar = 0
    for i in range (banyak_jenis):
        print("Jenis ke - ", str(i+1))
        #Input Kode potong
        list_kode.append(input("Masukkan Kode Potong (D/P/S) = "))
        #Inisialisasi Jenis Potong dan Harga sesuai kode potong
        if list_kode[i] == "D" or list_kode[i] == "d":
            jenis_potong = "Dada"
            harga = 2500
        elif list_kode[i] == "P" or list_kode[i] == "p":
            jenis_potong = "Paha"
            harga = 2000
        elif list_kode[i] == "S" or list_kode[i] == "s":
            jenis_potong = "Sayap"
            harga = 1000
        else:
            jenis_potong = "-"
            harga = 0
        list_jenis.append(jenis_potong)
        list_harga.append(harga)
        #Input Banyak Potong
        list_banyak.append(int(input("Masukkan Banyak Potong = ")))
        #Hitung jumlah yang harus dibayar
        list_jumlah.append(list_harga[i]*list_banyak[i])
        jumlah_bayar = jumlah_bayar + list_jumlah[i]
    #Input uang yang dibayar
    uang_bayar = int(input("Masukkan Uang Yang Dibayar = "))
    #Hitung pajak
    pajak = 0.1 * jumlah_bayar
    #Hitung total bayar
    total_bayar = jumlah_bayar + pajak
    #Hitung uang kembalian
    uang_kembalian = uang_bayar - total_bayar
    #Set output
    data = {
        "JENIS POTONG" : list_jenis,
        "HARGA SATUAN" : list_harga,
        "BANYAK BELI" : list_banyak,
        "JUMLAH BELI" : list_jumlah
    }
    data_order = pd.DataFrame(data)
    #Cetak Output
    print("AYAM DIGEPREK".center(60," "))
    print("="*60)
    print(data_order)
    print("="*60)
    print("\t\t\t Jumlah Bayar \t = \t Rp.%i" % (jumlah_bayar))
    print("\t\t\t Pajak \t\t = \t Rp.%i" % (pajak))
    print("\t\t\t Total Bayar \t = \t Rp.%i" % (total_bayar))
    print("Uang Anda \t = \t Rp.%i" % (uang_bayar))
    print("Uang Kembalian \t = \t Rp.%i" % (uang_kembalian))
    counter_kasir()
    
#Fungsi Counter kasir untuk mengulang
def counter_kasir():
    counter = input("Hitung lagi? (y/n) = ")
    if counter == "y":
        kasir()
    elif counter == "n":
        pertanyaan()     
    else:
        print("Input program salah harap ulangi")
        counter_kasir()
        
#Fungsi Tanya untuk kembali ke main menu
def pertanyaan():
    tanya = input("Kembali ke menu..? (y/n) = ")
    if tanya == "y":
        main_menu()
    elif tanya == "n":
        exit()
    else:
        print("Input salah, masukan input dengan benar")
        pertanyaan()

login()
