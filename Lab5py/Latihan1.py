print("List Pertama (a)")
print("====================================")
#List dengen 5 element
a = [90, 80, 70, 60, 50]

#Tampilkan element ke 3
print(a[2])
#Tampilkan element ke 2 sampai ke 4
print(a[1:4])
#Tampilkan element terakhir
print(a[4])

a[3] = 30
#Hasil Perubahan
print(a)
a[3:5] = [20, 10]
#Hasil Perubahan
print(a)

#Buat List kedua (b) dengan element 2 pertama mengambil dari list pertama (a)
print("List Kedua (b)")
print("====================================")
#List dengen 5 element
b = a[:2]
#Nilai List b
print(b)

#tambah list b dengan nilai string
b.append("ali")
#Hasil Perubahan
print(b)

#Tambah List b dengan 3 nilai
b.extend([34, 45, 56])
#Hasil Perubahan
print(b)

#Gabung List b dengan list a
b.extend(a)
#Hasil Penggabungan
print(b)


