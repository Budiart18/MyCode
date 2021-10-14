nim = input("Masukkan NIM = ")
nama = input("Masukkann Nama = ")
kelas = input("Masukkan Kelas = ")
matakuliah = input("Masukkan Mata Kuliah = ")

absen = int(input("Masukkan Nilai Absen = "))
tugas1 = int(input("Masukkan Nilai Tugas 1 = "))
tugas2 = int(input("Masukkan Nilai Tugas 2 = "))
uts = int(input("Masukkan Nilai UTS = "))
uas = int(input("Masukkan Nilai UAS = "))

jumlah = (absen*0.2) + (tugas1*0.1) + (tugas2*0.1) + (uts*0.3) + (uas*0.3)

if jumlah >= 80:
    grade = "A"
    lulus = "Anda Lulus"
elif jumlah >= 70:
    grade = "B"
    lulus = "Anda Lulus"
elif jumlah >= 60:
    grade = "C"
    lulus = "Anda Lulus"
elif jumlah >= 50:
    grade = "D"
    lulus = "Anda Tidak Lulus"
else:
    grade = "E"
    lulus = "Anda Tidak Lulus"

print("NIM = ", nim)
print("NAMA = ", nama)
print("KELAS = ", kelas)
print("MATA KULIAH = ", matakuliah)
print("===== DAFTAR NILAI =====")
print("Nilai Absen = ", absen)
print("Nilai Tugas 1 = ", tugas1)
print("Nilai Tugas 2 = ", tugas2)
print("Nilai UTS = ", uts)
print("Nilai UAS = ", uas)
print("========================")
print("Jumlah Nilai Anda = {:.2f}".format(jumlah))
print("Grade Nilai Anda = ", grade)
print(lulus)

# Anggota Kelompok
#   Syamsul bahri : 17210222
#   Muhammad Viqry Haikal : 17210373
#   Ragil Budiarto : 17211038
#   Arif Nur : 17211081
#   Solichin : 17210376
