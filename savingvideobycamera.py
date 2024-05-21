import cv2
import numpy as np

def compute_ssim(img1, img2):
    C1 = 6.5025
    C2 = 58.5225

    I1 = img1.astype(np.float32)
    I2 = img2.astype(np.float32)

    I2_2 = I2 ** 2
    I1_2 = I1 ** 2
    I1_I2 = I1 * I2

    mu1 = cv2.GaussianBlur(I1, (11, 11), 1.5)
    mu2 = cv2.GaussianBlur(I2, (11, 11), 1.5)

    mu1_2 = mu1 ** 2
    mu2_2 = mu2 ** 2
    mu1_mu2 = mu1 * mu2

    sigma1_2 = cv2.GaussianBlur(I1_2, (11, 11), 1.5)
    sigma1_2 -= mu1_2

    sigma2_2 = cv2.GaussianBlur(I2_2, (11, 11), 1.5)
    sigma2_2 -= mu2_2

    sigma12 = cv2.GaussianBlur(I1_I2, (11, 11), 1.5)
    sigma12 -= mu1_mu2

    t1 = 2 * mu1_mu2 + C1
    t2 = 2 * sigma12 + C2
    t3 = t1 * t2

    t1 = mu1_2 + mu2_2 + C1
    t2 = sigma1_2 + sigma2_2 + C2
    t1 = t1 * t2

    ssim_map = t3 / t1
    mssim = cv2.mean(ssim_map)

    return mssim[0]

def main():
    img1 = cv2.imread("frame_0.jpg", cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread("frame_5842.jpg", cv2.IMREAD_GRAYSCALE)

    if img1 is None or img2 is None:
        print("Could not open or find the image")
        return

    ssim_value = compute_ssim(img1, img2)
    print(f"SSIM: {ssim_value}")

if __name__ == "__main__":
    main()
