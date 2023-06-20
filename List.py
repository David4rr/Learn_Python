# List menggunakan []

nama = ["Akbar", "Akber", "Akber esten"]
nama.append("Akber Winet") # Menambahkan data list

print (nama[0]) # Untuk memanggil index dan dimulai dari 0
print (len(nama)) # Untuk mengetahui jumlah data dalam list

nama.remove("Akbar") # Mengahpus data list
print (nama)
print (len(nama))

nama[0] = "Akber Wikwok" # Mengubah data list
print (nama)

# For Loop
for nama_pelanggan in nama: # Semua data nama akan dimasukan ke variable nama_pelanggan
    print (nama_pelanggan)

# Range
nomor = range(1, 11) # Untuk menampilkan batas 10 maka harus dilebihkan 1 yaitu 11
# range digunakan untuk mempermudah penginputan list

for nomor_urut in nomor:
    print (nomor_urut)

# Range versi 2
for no in range(1, 11):
    print (no)

#! Saat Menghapus data perhatikan posisi indeks bisa saja berubah