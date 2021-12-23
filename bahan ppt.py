import pandas as pd

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Fungsi Login (User = admin, Password = admin)
def login():
    print("=" * 45)
    print("Halaman Login Kasir Ayam Digeprek")
    username = input("Masukan Username: ")
    password = input("Masukan Password: ")
    if username == "admin" and password == "admin":
        print("Login berhasil...")
        print("=" *45)
        main_menu()
    else:
        print("Login gagal. Silahkan coba lagi...")
        print("=" * 45)
        login()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
#Perkenalan anggota menggunakan OOP
class mahasiswa:    
    def __init__(self, nama, nim):
        self.nim = nim
        self.nama = nama
    def perkenalan(self):
        print(f" => {self.nama} ({self.nim})")
mhs1 = mahasiswa("Arif Nur","17211081")
mhs2 = mahasiswa("Ragil Budiarto","17211038")
mhs3 = mahasiswa("Solichin","17210376")
mhs4 = mahasiswa("Syamsul Bahri","17210222")
mhs5 = mahasiswa("Muhammad Viqry Haikal","17210373")
def anggota():
    print("\n")
    print(" ANGGOTA KELOMPOK 3 ".center(45,"="))
    print(" KELAS 17.1C.12 ".center(45,"="))
    mhs1.perkenalan()
    mhs2.perkenalan()
    mhs3.perkenalan()
    mhs4.perkenalan()
    mhs5.perkenalan()
    print("="*45) 
    pertanyaan()

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Fungsi Main menu kasir
def main_menu():
    print("\n")
    print(" MAIN MENU AYAM DIGEPREK ".center(45,"="))
    print("Selamat Datang Di Ayam Digeprek".center(45,"="))
    print(" Masukan Input Aplikasi ".center(45,"="))
    print("1. Daftar Harga")
    print("2. Kasir")
    print("3. Anggota")
    print("4. Exit")
    print("="*45) 
    
    # input pilihan
    pilihan = input("Pilih menu (1/2/3) = ")
    
    # pilihan menu
    if pilihan == "1":
        daftar_harga()
    elif pilihan == "2":
        kasir()
    elif pilihan == "3":
        anggota()
    else:
        print("Program Exit")
        exit()

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Fungsi Daftar harga     
def daftar_harga():
    print("\n")
    print("="*45)
    print("DAFTAR HARGA AYAM DIGEPREK".center(45," "))
    print("="*45)
    print("NO. \t JENIS \t\t HARGA SATUAN")
    print("1. \t DADA \t\t Rp. 25.000")
    print("2. \t PAHA \t\t Rp. 20.000")
    print("3. \t SAYAP \t\t Rp. 15.000")
    print("="*45)
    pertanyaan()

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++              
#Fungsi Kasir
def kasir():
    print("\n")
    
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
            harga = 25000
        elif list_kode[i] == "P" or list_kode[i] == "p":
            jenis_potong = "Paha"
            harga = 20000
        elif list_kode[i] == "S" or list_kode[i] == "s":
            jenis_potong = "Sayap"
            harga = 15000
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
    
    #Hitung pajak
    pajak = 0.1 * jumlah_bayar
    
    #Hitung total bayar
    total_bayar = jumlah_bayar + pajak
    #Print total bayar
    print(f"Total Bayar = {total_bayar} ")
    
    #Input uang yang dibayar
    uang_bayar = int(input("Masukkan Uang Yang Dibayar = "))
    
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
    print("\n")
    print("AYAM DIGEPREK".center(60," "))
    print("="*60)
    print(data_order)
    print("="*60)
    print(f"\t\t\t Jumlah Bayar \t = \t Rp.{jumlah_bayar}")
    print(f"\t\t\t Pajak \t\t = \t Rp.{pajak}")
    print(f"\t\t\t Total Bayar \t = \t Rp.{total_bayar}")
    print(f"Uang Anda \t = \t Rp.{uang_bayar}")
    print(f"Uang Kembalian \t = \t Rp.{uang_kembalian}")
    print("\n")
    ulang_kasir()


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Fungsi untuk mengulang kasir
def ulang_kasir():
    ulang = input("Hitung lagi? (y/n) = ")
    if ulang == "y":
        kasir()
    elif ulang == "n":
        pertanyaan()     
    else:
        print("Input program salah harap ulangi")
        ulang_kasir()

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
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
