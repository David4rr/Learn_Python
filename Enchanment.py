import cv2
from matplotlib import pyplot as plt

# Baca gambar
gambar = cv2.imread('C:/Users/david/Documents/my private document/tugas kuliah/Semester 5/Workshop Pengolahan Citra dan Vision/Bahan Image/test.jpeg')

# Ubah ke citra grayscale
gambarenchan = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

# Lakukan histogram equalization
HQ = cv2.equalizeHist(gambarenchan)

# Tentukan ukuran subplot dan jarak
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
fig.subplots_adjust(wspace=0.5)  # Sesuaikan jarak antar subplot

# Tampilkan gambar asli, citra grayscale, dan hasil histogram equalization
axs[0].imshow(cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB))
axs[0].set_title('Citra Asli')

axs[1].imshow(gambarenchan, cmap='gray')
axs[1].set_title('Citra Grayscale')

axs[2].imshow(HQ, cmap='gray')
axs[2].set_title('Hist. Equalization')

plt.show()