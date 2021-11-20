import pandas as pd
#variabel yg berulang menggunakan list/matrix
list_nim = []
list_nama = []
list_absen = []
list_tugas = []
list_uts = []
list_uas =[]
list_total = []
list_grade = []
list_keterangan = []

#berapa kali input data diulang
ulang = 2

#input data
for i in range (ulang):
    print("Data ke - ", str(i+1))
    list_nim.append(input("NIM : "))
    list_nama.append(input("NAMA : "))
    list_absen.append(float(input("Nilai Absen : ")))
    list_tugas.append(float(input("Nilai Tugas : ")))
    list_uts.append(float(input("Nilai UTS : ")))
    list_uas.append(float(input("Nilai UAS : ")))
    
#proses perhitungan total,grading, dan pemberian keterangan 
for i in range (ulang):
    list_total.append((list_absen[i]*0.1)+(list_tugas[i]*0.2)+(list_uts[i]*0.3)+(list_uas[i]*0.4))
    if list_total[i] >= 80:
        grade = "A"
        keterangan = "Lulus"
    elif list_total[i] >= 70:
        grade = "B"
        keterangan = "Lulus"
    elif list_total[i] >= 60:
        grade = "C"
        keterangan = "Lulus"
    elif list_total[i] >= 50:
        grade = "D"
        keterangan = "Tidak Lulus"
    else:
        grade = "E"
        keterangan = "Tidak Lulus"
    list_grade.append(grade)
    list_keterangan.append(keterangan)

#Set output
nilai = {
    "NIM" : list_nim,
    "NAMA" : list_nama,
    "Nilai Absen" : list_absen,
    "Nilai Tugas" : list_tugas,
    "Nilai UTS" : list_uts,
    "Nilai UAS" : list_uas,
    "Total" : list_total,
    "Grade" : list_grade,
    "Keterangan" : list_keterangan
}
data_nilai = pd.DataFrame(nilai)

#Cetak Output
print(" DAFTAR NILAI ".center(100,"="))
print(data_nilai)
print("="*100)
