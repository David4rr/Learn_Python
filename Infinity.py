from turtle import * 
# Untuk mengimpor semua fungsi dan konstanta yang ada dalam modul "turtle"
# ke dalam program kita. 

bgcolor("black") # Mengatur warna background
color("cyan") # Mengubah warna 
speed(1) # mengatur kecepatan
right(45) # mengubah arah turtle sebesar 45 derajat kearah kanan
for i in range(150): # perulangan sebanyak 150 kali
    circle(30) # menggambar lingkarang dengan jari - jari 30
    if 7 < i < 62: 
        left(5) # Jika nilai i berada di antara 7 dan 62, maka turtle akan berputar 5 derajat ke kiri.
    if 80 < i < 133:
        right(5) # Jika nilai i berada di antara 80 dan 133, maka turtle akan berputar 5 derajat ke kanan.
    if i < 80:
        forward(10) # Jika nilai i kurang dari 80, maka turtle akan maju sejauh 10 piksel.
    else:
        forward(5) # Jika kondisi di atas tidak terpenuhi (nilai i lebih besar atau sama dengan 80), maka turtle akan maju sejauh 5 piksel.