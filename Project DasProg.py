def login():
    print('=' * 20)
    print('Halaman Login Kasir Ayam Digeprek')
    username = input('masukan username kasir anda: ')
    password = input('masukan password: ')
    if username == 'admin' and password == 'adminpass':
        print('login berhasil...\n\n')
        kasir()
    else:
        print('login gagal coba lagi..')
        login()
        
def kasir():
    print("AYAM DIGEPREK".center(70," "))
    print("="*70)
    print('''No. \t Jenis \t\t Harga \t\t Banyak \t Jumlah
    \t Potong \t Satuan \t Beli \t\t Harga''')
    print("="*70)
    banyak_jenis = int(input("Masukkan Banyak Jenis = "))
    jenis_ke = 1
    jumlah_bayar = 0
    while (jenis_ke <= banyak_jenis):
        kode_potong = input("Masukkan Kode Potong (D/P/S) = ")
        if kode_potong == "D" or kode_potong == "d":
            jenis_potong = "Dada"
            harga = 2500
        elif kode_potong == "P" or kode_potong == "p":
            jenis_potong = "Paha"
            harga = 2000
        elif kode_potong == "S" or kode_potong == "s":
            jenis_potong = "Sayap"
            harga = 1000
        else:
            jenis_potong = "-"
            harga = 0
        banyak_potong = int(input("Masukkan Banyak Potong = "))
        jumlah_harga = harga * banyak_potong
        print("%i \t %s \t\t %i \t\t %i \t\t Rp.%i" % (jenis_ke,jenis_potong,harga,banyak_potong,jumlah_harga))
        jumlah_bayar = jumlah_bayar + jumlah_harga
        jenis_ke = jenis_ke + 1
    print("="*70)
    print("\t\t\t\t Jumlah Bayar \t = \t Rp.%i" % (jumlah_bayar))
    pajak = jumlah_bayar*10/100
    print("\t\t\t\t Pajak \t\t = \t Rp.%i" % (pajak))
    total_bayar = jumlah_bayar + pajak
    print("\t\t\t\t Total Bayar \t = \t Rp.%i" % (total_bayar))
    
login()
