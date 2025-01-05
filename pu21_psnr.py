import sys
import cv2
import numpy as np
import imageio.v2 as imageio  # Import imageio for HDR files

def psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 1.0  # Assuming images are normalized to [0, 1]
    return 10 * np.log10(max_pixel ** 2 / mse)

def convert_to_pu_space(image, gamma=2.2):
    return np.power(image / 255.0, 1 / gamma)

def compute_pu21_psnr(sdr_image_path, hdr_image_path):
    # Read SDR image
    sdr_img = cv2.imread(sdr_image_path, cv2.IMREAD_COLOR)
    if sdr_img is None:
        raise ValueError(f"Could not open or find the SDR image at {sdr_image_path}")
    sdr_img = cv2.cvtColor(sdr_img, cv2.COLOR_BGR2RGB) / 255.0

    # Read HDR image
    hdr_img = imageio.imread(hdr_image_path, format='HDR-FI')
    if hdr_img is None:
        raise ValueError(f"Could not open or find the HDR image at {hdr_image_path}")
    hdr_img = hdr_img / hdr_img.max()  # Normalize HDR image to [0, 1]

    # Convert to PU space
    pu_sdr = convert_to_pu_space(sdr_img)
    pu_hdr = convert_to_pu_space(hdr_img)

    # Calculate PSNR in PU space
    return psnr(pu_sdr, pu_hdr)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pu21_psnr.py <sdr_image_path> <hdr_image_path>")
        sys.exit(1)
    
    sdr_image_path = sys.argv[1]
    hdr_image_path = sys.argv[2]
    try:
        pu21_psnr_score = compute_pu21_psnr(sdr_image_path, hdr_image_path)
        print(f"PU21-PSNR Score: {pu21_psnr_score}")
    except ValueError as e:
        print(e)
