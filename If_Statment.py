# If-Statment
# Pengkondisian
#! Tab dalam Python sangat berpengaruh terhadap jalanya Code

# Contoh 1
manusia = 100
zombie = 100

if manusia < zombie:
    print ("Manusia Punah")

if manusia > zombie:
    print ("Manusia Selamat")

if manusia == zombie:
    print ("Perang Berkepanjangan")

# Contoh 2
menang = True

if menang == True:
    print ("Selamat anda menang")

if menang == False:
    print ("Silahkan coba lagi")

#! Output yang dihasilkan adalah Output yang bernilai true


# If
menang2 = False

if menang2:
    print ("Selamat anda mendapatkan uang")
else:
    print("Awikwok bang")

# else if => elif jika di python

Pilih_menu = input ("Pilih menu dari 1-3 : ")

if Pilih_menu == "1":
    print("Ayam")
elif Pilih_menu == "2":
    print ("Sate")
elif Pilih_menu == "3":
    print ("Rendang")
else:
    print ("Menu tidak Tersedia")

# if kondisi:
#    melakukan apa?
#    melakukan hal lain
# dst #! Jika tidak menggunakan tab maka baris code tersebut tidak akan di jalankan