import matplotlib.pyplot as plt
import numpy as np
from skimage import io, exposure
from skimage.color import rgb2gray

# Load the image
image = io.imread('C:/Users/david/Documents/my private document/tugas kuliah/Semester 5/Workshop Pengolahan Citra dan Vision/Bahan Image/Daun.jpeg')

# Convert the image to grayscale
gray_image = rgb2gray(image)
bright = gray_image + 50 
dark = gray_image - 50
# contrast = (gray_image)

# Apply contrast stretching
p2, p98 = np.percentile(gray_image, (2, 98))
contrast = exposure.rescale_intensity(gray_image, in_range=(p2, p98))

# Create the figure and subplots
fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(5, 5))
# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.3, hspace=0.5)

# Display the original image
axs[0, 0].imshow(image)
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

# Display the grayscale image
axs[0, 1].imshow(gray_image, cmap='gray')
axs[0, 1].set_title('Grayscale Image')
axs[0, 1].axis('off')

# Display the bright image
axs[0, 2].imshow(bright, cmap='gray')
axs[0, 2].set_title('Bright Image')
axs[0, 2].axis('off')

# Display the dark image
axs[1, 0].imshow(dark, cmap='gray')
axs[1, 0].set_title('Dark Image')
axs[1, 0].axis('off')

# Create the histogram of dark image
axs[1, 1].hist(dark.ravel(), bins=256)
axs[1, 1].set_xlabel('Pixel Intensity')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_title('Dark Image Histogram')

# Create the histogram of bright image
axs[1, 2].hist(bright.ravel(), bins=256)
axs[1, 2].set_xlabel('Pixel Intensity')
axs[1, 2].set_ylabel('Frequency')
axs[1, 2].set_title('Bright Image Histogram')

# Display the contrast-stretched image
axs[2, 0].imshow(contrast, cmap='gray')
axs[2, 0].set_title('Contrast-Stretched Image')
axs[2, 0].axis('off')

# Create the histogram of contrast-stretched image
axs[2, 1].hist(contrast.ravel(), bins=256)
axs[2, 1].set_xlabel('Pixel Intensity')
axs[2, 1].set_ylabel('Frequency')
axs[2, 1].set_title('Contrast-Stretched Image Histogram')

# Show the plot
plt.show()