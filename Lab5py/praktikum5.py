
#Mengimport Modul PrettyTabel
from prettytable import PrettyTable

print("Program data Mahasiswa")
print()

#Membuat Tabel yang diperlukan
Tabel = PrettyTable(["No", "Nama", "NIM", "Nilai Tugas", "Nilai UTS", "Nilai UAS", "Nilai Akhir"])

#Deklarasi untuk no 
no = int(0)

#Kondisi Perulangan jika pilih = 'y' maka true dan akan mengulang program
pilih = 'y'

while True:
    #Inputan untuk mengisi tabel
    no += 1
    nama = input("Masukan Nama \t \t = ")
    nim = input("Masukan NIM \t \t = ")
    tugas = int(input("Masukan Nilai Tugas \t = "))
    uts = int(input("Masukan Nilai UTS \t = "))
    uas = int(input("Masukan Nil(ai UTS \t = "))
    akhir = "{:.2f}".format((tugas*.30) + (uts*.35) + (uas*.35))

    #Menambahkan inputan user ke tabel yang sudah di buat
    Tabel.add_row([no,nama,nim,tugas,uts,uas,akhir])

    Tabel.horizontal_char = "="

    Tabel.junction_char = "~"

    #Input Pilihan jika user menginputkan y maka pilih = 'y' / true / mengulang program
    #Inputan Pilihan jika user menginputkan n maka pilih ='n' / false / Program berhenti
    pilih = input("Apakah Ingin Memasukan data lagi? y/t \t = ")
    if pilih == 't':
            break

#Untuk menampilkan tabel yang sudah di buat di atas
print(Tabel)


