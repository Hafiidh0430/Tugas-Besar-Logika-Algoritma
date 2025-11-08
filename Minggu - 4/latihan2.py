# inisialisasi input range_angka matrix
range_angka = int(input("Range Angka: "))

# inisialisasi matriks kosong
matriks = []

# blok for i matrix = pada bagian ini akan membuat matrix ordo 3x3 sesuai dengan ketentuan yang diberikan
# loop baris matrix dengan ordo 3x3
for i in range(3):
    # inisialisasi baris kosong
    baris = []
    # blok for j matrix = pada bagian ini akan mengisi setiap kolom dalam baris sesuai dengan ketentuan yang diberikan
    # loop untuk setiap kolom dalam baris
    for j in range(3):
        # jika nilai i == j, maka isi nilai = 0
        if i == j:
            nilai = 0
        # jika i < j, maka isi nilai = range_angka + j
        elif i < j:
            nilai = range_angka + j
        # jika tidak keduanya, maka isi nilai = i
        else:
            nilai = i
        # tambahkan nilai ke dalam baris
        baris.append(nilai)
    # tambahkan baris ke dalam matriks
    matriks.append(baris)

# tampilkan hasil matrix
print("Hasil Matrix:")

# loop setiap baris dalam matriks
for baris in matriks:
    # tampilkan baris
    print(baris)
