nama = input("Nama Penyewa: ")
jenis_ps = input("Jenis PS [PS3/PS4/PS5]: ")
sewa_perjam = int(input("Harga Sewa [Jam]: "))
sewa_perhari = int(input("Harga Sewa [Hari]: "))
# total_transaksi = int(input("Lama Sewa [x]: "))

total_lama, total_harga_perjam, total_harga_perhari = 0, 0, 0

data_ps = [
    {"jenis_ps": "PS3", "harga_perjam": 20000, "harga_perhari": 400000},
    {"jenis_ps": "PS4", "harga_perjam": 25000, "harga_perhari": 500000},
    {"jenis_ps": "PS5", "harga_perjam": 30000, "harga_perhari": 600000},
]

data_transaksi = []

for ps in data_ps:
   if jenis_ps.lower() == ps['jenis_ps'].lower():
      if sewa_perjam > 0:
        if sewa_perjam > 3:
            total_harga_perjam = (ps['harga_perjam'] * 0.05) * sewa_perjam
        else:
            total_harga_perjam = ps['harga_perjam'] * sewa_perjam
      
      if sewa_perhari > 0:
          if sewa_perhari > 3:
              total_harga_perhari = (ps['harga_perhari'] * 0.15) * sewa_perhari
          else:
              total_harga_perhari = ps['harga_perhari'] * sewa_perhari
          
print(total_harga_perjam)
print(total_harga_perhari)
              
          
          
           
          


