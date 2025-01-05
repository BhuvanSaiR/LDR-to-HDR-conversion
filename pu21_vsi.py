import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim

def convert_to_pu21(image):
    """Convert an image to the perceptually uniform PU21 space."""
    return np.power(image, 1 / 2.2)

def compute_pu21_vsi(img1, img2):
    """Compute the Visual Saliency Index (VSI) between two images in PU21 space."""
    # Convert both images to grayscale if needed
    if img1.ndim == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    if img2.ndim == 3:
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # Normalize images to [0, 1]
    img1 = img1 / 255.0
    img2 = img2 / 255.0

    # Convert images to PU21 space
    pu_img1 = convert_to_pu21(img1)
    pu_img2 = convert_to_pu21(img2)

    # Specify data range for SSIM
    data_range = 1.0  # Assuming normalized images

    # Calculate VSI-like score using Structural Similarity Index (SSIM) as a proxy
    ssim_score, _ = ssim(pu_img1, pu_img2, full=True, data_range=data_range)
    return ssim_score

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python pu21_vsi.py <image1_path> <image2_path>")
        sys.exit(1)

    image1_path = sys.argv[1]
    image2_path = sys.argv[2]

    # Load images
    image1 = cv2.imread(image1_path, cv2.IMREAD_COLOR)
    image2 = cv2.imread(image2_path, cv2.IMREAD_COLOR)

    # Compute PU21-VSI
    pu21_vsi_score = compute_pu21_vsi(image1, image2)
    print(f"PU21-VSI Score: {pu21_vsi_score}")
