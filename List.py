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

#! Saat Menghapus data perhatikan posisi indeks bisa saja berubah