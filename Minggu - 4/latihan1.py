# inisialisasi data harga sewa PS
data_ps = [
    {"jenis_ps": "PS3", "harga_perjam": 20000, "harga_perhari": 400000},
    {"jenis_ps": "PS4", "harga_perjam": 25000, "harga_perhari": 500000},
    {"jenis_ps": "PS5", "harga_perjam": 30000, "harga_perhari": 600000},
]

# inisialisasi total harga jam/hari
total_harga_perjam, total_harga_perhari = 0, 0

# inisialisasi list data transaksi
data_transaksi = []

# inisialisasi variabel sewa lagi
is_sewa_lagi = "YA"

# inisialisasi diskon dan bonus
diskon_perjam = 0.05
diskon_perhari = 0.15
bonus_jam = 2

# loop selama user ingin menyewa lagi
while is_sewa_lagi == "YA":
    
    # inisialisasi transaksi_ke
    transaksi_ke = 0
    
    # input data penyewa
    nama = input("Nama Penyewa: ")
    jenis_ps = input("Jenis PS [PS3/PS4/PS5]: ")
    
    # loop data ps dan cocokkan dengan input jenis_ps
    for ps in data_ps:
        
        # jika jenis ps cocok
        if jenis_ps.upper() == ps['jenis_ps']:
            
            # inisialisasi input lama sewa
            sewa_perjam = int(input("Harga Sewa [Jam]: "))
            sewa_perhari = int(input("Harga Sewa [Hari]: "))
            
            # jika sewa perjam/haru > 0
            if sewa_perjam > 0:
                
                # jika sewa perjam > 3, maka dapat dan hitung diskon
                if sewa_perjam > 3:
                   total_harga_perjam = ps["harga_perjam"] * sewa_perjam * (1 - diskon_perjam)
                   
                # jika tidak, maka tidak dapat diskon
                else:
                    total_harga_perjam = ps['harga_perjam'] * sewa_perjam
            
            # jika sewa perhari > 0
            if sewa_perhari > 0:
                
                # jika sewa perhari > 3, maka dapat dan hitung diskon
                if sewa_perhari > 3:
                    total_harga_perhari = ps["harga_perhari"] * sewa_perhari * (1 - diskon_perhari)
                    
                # jika tidak, maka tidak dapat diskon
                else:
                    total_harga_perhari = ps['harga_perhari'] * sewa_perhari
            
            # loop dan cek transaksi ke berapa
            for transaksi in data_transaksi:
                
                #  cek, jika nama sama dengan data transaksi sebelumnya
                if transaksi["nama"].lower() == nama.lower():
                    
                    # tambah 1 transaksi_ke
                    transaksi_ke += 1
                    
                    # jika transaksi ke 6/ > 5, maka berikan bonus 2 jam sewa
                    if transaksi["transaksi_ke"] == 6:
                        transaksi["sewa_perjam"] += bonus_jam
                        
            # jika transaksi ke masih 0, maka set ke 1
            else:
                transaksi_ke += 1
                
            # simpan data transaksi ke dalam data_transaksi dan break loop
            data_transaksi.append({
                "nama": nama,
                "jenis_ps": jenis_ps,
                "sewa_perjam": sewa_perjam,
                "sewa_perhari": sewa_perhari,
                "total_harga_perjam": total_harga_perjam,
                "total_harga_perhari": total_harga_perhari,
                "total_bayar": total_harga_perjam + total_harga_perhari,
                "transaksi_ke": transaksi_ke,
            })
            break
    # jika jenis ps tidak tersedia, maka ulangi (continue)
    else:
        print("Jenis PS tidak tersedia! Coba lagi.")
        continue  
         
    # apakah ingin menyewa lagi? jika iya, maka akan ulangi loop
    is_sewa_lagi = input("Apakah Ingin Menyewa Lagi? [YA/TIDAK]: ").upper()
          
# tampilkan data transaksi
print("\n==================================== DATA TRANSAKSI ====================================")
print("No\tNama\t\tJenis PS\tJam\tHari\tTotal/Jam\tTotal/Hari\tTotal Bayar\tTotal/Transaksi-Ke")
print("==========================================================================================")

# loop dan tampilkan isi data_transaksi
for i, d in enumerate(data_transaksi, start=1):
    print(f"{i}\t{d['nama']}\t\t{d['jenis_ps']}\t\t{d['sewa_perjam']}\t{d['sewa_perhari']}\t"
          f"{d['total_harga_perjam']}\t\t{d['total_harga_perhari']}\t\t{d['total_bayar']}\t\t{d['transaksi_ke']}")

print("==========================================================================================")