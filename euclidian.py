from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

# Create a subplot grid
nrows = 4 # Number of rows
ncols = 5 # Number of columns
fig, axes = plt.subplots(nrows=nrows, ncols=ncols)

# Function to calculate Manhattan Distance between two images
def euclidean_distance(img1, img2):
    # Convert images to NumPy arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    # Calculate Euclidean Distance
    distance = np.sqrt(np.sum(np.square(arr1 - arr2)))

    return distance


# Folder path containing the RGB images
rgb_folder_path = "D:/For Me only/Perkuliahan dan Organisasi/Semester 4/Pengenalan Pola/UTS\Hasil kompress"

# Load the comparison image (grayscale)
comp_img = Image.open("D:/For Me only/Perkuliahan dan Organisasi/Semester 4/Pengenalan Pola/UTS/gray/objek_pembanding.jpg").convert('L')

# Initialize variables for storing the closest image and its distance
closest_img = None
closest_distance = float('inf')

# Loop through each file in the folder
for i, filename in enumerate(os.listdir(rgb_folder_path)):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Filter only image files
        # Load the RGB image
        rgb_img = Image.open(os.path.join(rgb_folder_path, filename))

        # Convert the RGB image to grayscale
        gray_img = rgb_img.convert('L')

        # Get the subplot index based on the current loop iteration
        row_idx = i // ncols
        col_idx = i % ncols

        # Check if the subplot index is within bounds
        if row_idx < nrows and col_idx < ncols:

            # Calculate the Manhattan Distance between the grayscale image and the comparison image
            distance = euclidean_distance(gray_img, comp_img)

            # Display the grayscale image in the current subplot
            axes[row_idx][col_idx].imshow(np.asarray(gray_img), cmap='gray')
            title = f"{filename} ({distance:.2f})"
            axes[row_idx][col_idx].set_title(title, pad=1)
            axes[row_idx][col_idx].axis('off')

            # Check if the current distance is closer than the closest distance so far
            if distance < closest_distance:
                closest_distance = distance
                closest_img = rgb_img


# Save the closest image
# plt.imshow(closest_img)
gambar_terdekat = closest_img.convert('L')
gambar_terdekat.save("closest_image.jpg")

# Add a new subplot for the closest image
ax = axes[nrows-1][ncols-1]

# Display the closest image on the new subplot
ax.imshow(np.asarray(gambar_terdekat), cmap='gray')
title = f"Closest Image"
ax.set_title(title, pad=1)
ax.axis('off')

# Add a new subplot for the Objek Pembanding
ax = axes[nrows-1][ncols-2]
ax.imshow(np.asarray(comp_img), cmap='gray')
title = f"Objek Pembanding"
ax.set_title(title, pad=1)
ax.axis('off')


# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.4, hspace=0.4)

# Show the plot
plt.show()