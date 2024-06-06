from turtle import *

def draw_love():
    speed(3)
    color('red')
    pensize(3)

    # Menutup bentuk dengan warna merah
    begin_fill()
    left(50)
    forward(133)
    circle(50, 200)
    right(140)
    circle(50, 200)
    forward(133)
    end_fill()

# Menggambar pola "LOVE"
draw_love()

# Menulis teks "LOVE" di atas gambar
penup()
goto(0, 80)
pendown()
color('black')
write("fill_urName", align='center', font=('Arial', 35, 'bold'))

# Menunggu sampai jendela turtle ditutup
done()
