import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray

# Load the image
image = io.imread('C:/Users/david/Documents/my private document/tugas kuliah/Semester 5/Workshop Pengolahan Citra dan Vision/Bahan Image/Daun.jpeg')

# Convert the image to grayscale
gray_image = rgb2gray(image)
negasi_image = 255 - gray_image

# Create the figure and subplots
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

# Display the original image
axs[0, 0].imshow(image)
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

# Display the grayscale image
axs[0, 1].imshow(gray_image, cmap='gray')
axs[0, 1].set_title('Grayscale Image')
axs[0, 1].axis('off')

# Display the negative image
axs[1, 0].imshow(negasi_image, cmap='gray')
axs[1, 0].set_title('Negative Image')
axs[1, 0].axis('off')

# Create the histogram of negative image
axs[1, 1].hist(negasi_image.ravel(), bins=256)
axs[1, 1].set_xlabel('Pixel Intensity')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_title('Negative Image Histogram')

# Show the plot
plt.show()