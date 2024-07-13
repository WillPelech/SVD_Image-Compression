# import numpy as np
# import os
# from PIL import Image
# from matplotlib import pyplot as plt

# # Paths
# image_path = '/Users/willpelech/Desktop/S/random.png'
# save_path = '/Users/willpelech/Desktop/S/compressed.png'

# # Ensure the directory exists
# if not os.path.exists(os.path.dirname(save_path)):
#     os.makedirs(os.path.dirname(save_path))
#     print("Created directory:", os.path.dirname(save_path))

# try:
#     # Load image
#     print("Loading image...")
#     image = Image.open(image_path)
#     grey_img = image.convert('L')
#     imatrix = np.array(grey_img, dtype=float)

#     # Perform SVD
#     print("Performing SVD...")
#     U, s, Vt = np.linalg.svd(imatrix, full_matrices=False)
#     S = np.diag(s[:9])
#     U = U[:, :9]
#     Vt = Vt[:9, :]

#     # Image reconstruction and saving
#     print("Reconstructing and saving image...")
#     plt.imshow(U @ S @ Vt, cmap='gray')
#     plt.savefig(save_path)
#     print("Image saved at:", save_path)
#     plt.show()

# except Exception as e:
#     print("Failed to process the image:", e)
import os

# Define the path where you want to save the file
save_path = '/Users/willpelech/Desktop/SVD/test_file.txt'

# Ensure the directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)

try:
    # Write a test file
    with open(save_path, 'w') as f:
        f.write('This is a test file.')
    print(f"File successfully saved at {save_path}")
except Exception as e:
    print(f"Failed to save file: {e}")
