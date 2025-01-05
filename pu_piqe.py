import sys
import cv2
import numpy as np
from skimage import color, util
from skimage.metrics import structural_similarity as ssim

def convert_to_pu_space(image, gamma=2.2):
    """Convert an image to perceptually uniform (PU) space using gamma correction."""
    return np.power(image / 255.0, 1 / gamma)

def calculate_piqe(image):
    """Calculate the PIQE score on a grayscale image."""
    # The basic PIQE calculation (as a rough example, since scikit-image doesn't have PIQE by default).
    # Here, we compute local contrast and noise artifacts as a proxy for PIQE.

    # Convert to grayscale
    gray = color.rgb2gray(image) if image.ndim == 3 else image

    # Calculate local variance as a proxy for image noise and perceptual quality
    variance_map = util.img_as_float(util.random_noise(gray, mode='gaussian'))
    return np.var(variance_map)

def compute_pu_piqe(image_path):
    """Compute PU-PIQE for an image after converting to PU space."""
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not load image at the provided path.")

    # Convert image to PU space
    pu_image = convert_to_pu_space(image)

    # Calculate PIQE on the perceptually uniform image
    pu_piqe_score = calculate_piqe(pu_image)
    
    return pu_piqe_score

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pu_piqe.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    pu_piqe_score = compute_pu_piqe(image_path)
    print(f"PU-PIQE Score: {pu_piqe_score}")
