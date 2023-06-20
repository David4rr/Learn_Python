#! Ada seorang client ingin menginputkan data nama dan umur dengan jumlah yang dia inginkan !

banyak = int(input("Berapa banyak data yang Anda inginkan ? "))

nama = []
umur = []

for i in range(1, banyak + 1):
    print (f"Data ke {i}")
    input_nama = input("Nama :")
    input_umur = int(input("Umur :"))

    nama.append(input_nama)
    umur.append(input_umur)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print (f"{data_nama} Berumur {data_umur} Tahun")