import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
import os


def read_img(img_path):
    """
        Read grayscale image
        Inputs:
        img_path: str: image path
        Returns:
        img: cv2 image
    """
    return cv2.imread(img_path, 0)


def padding_img(img, filter_size=3):
    """
    The surrogate function for the filter functions.
    The goal of the function: replicate padding the image such that when applying the kernel with the size of filter_size, the padded image will be the same size as the original image.
    WARNING: Do not use the exterior functions from available libraries such as OpenCV, scikit-image, etc. Just do from scratch using function from the numpy library or functions in pure Python.
    Inputs:
        img: cv2 image: original image
        filter_size: int: size of square filter
    Return:
        padded_img: cv2 image: the padding image
    """
    padded_img = np.pad(img, ((filter_size//2, filter_size//2), (filter_size//2, filter_size//2)), mode='edge')
    return padded_img

def mean_filter(img, filter_size=3):
    """
    Smoothing image with mean square filter with the size of filter_size. Use replicate padding for the image.
    WARNING: Do not use the exterior functions from available libraries such as OpenCV, scikit-image, etc. Just do from scratch using function from the numpy library or functions in pure Python.
    Inputs:
        img: cv2 image: original image
        filter_size: int: size of square filter,
    Return:
        smoothed_img: cv2 image: the smoothed image with mean filter.
    """
    # Padding the image
    padded_img = padding_img(img, filter_size)
    # Initialize smoothed image
    smoothed_img = np.zeros_like(img)
    # Get the height and width of the input image
    h, w = img.shape
    
    # Loop through each pixel of the input image
    for i in range(h):
        for j in range(w):
            # Compute the mean value of the pixel's neighborhood defined by the filter size
            smoothed_img[i, j] = np.mean(padded_img[i:i+filter_size, j:j+filter_size])
    return smoothed_img

def median_filter(img, filter_size=3):
    """
    Smoothing image with median square filter with the size of filter_size. Use replicate padding for the image.
    WARNING: Do not use the exterior functions from available libraries such as OpenCV, scikit-image, etc. Just do from scratch using function from the numpy library or functions in pure Python.
    Inputs:
        img: cv2 image: original image
        filter_size: int: size of square filter
    Return:
        smoothed_img: cv2 image: the smoothed image with median filter.
    """
    # Padding the image
    padded_img = padding_img(img, filter_size)
    # Initialize smoothed image with the same size as the input image
    smoothed_img = np.zeros_like(img)
    # Get the height and width of the input image
    h, w = img.shape
    
    # Loop through each pixel of the input image
    for i in range(h):
        for j in range(w):
            # Compute the median value of the pixel's neighborhood defined by the filter size
            smoothed_img[i, j] = np.median(padded_img[i:i+filter_size, j:j+filter_size])
    return smoothed_img


def psnr(gt_img, smooth_img):
    """
        Calculate the PSNR metric
        Inputs:
            gt_img: cv2 image: groundtruth image
            smooth_img: cv2 image: smoothed image
        Outputs:
            psnr_score: PSNR score
    """
    # Calculate the Mean Squared Error (MSE)
    mse = np.mean((gt_img - smooth_img) ** 2)
    if mse == 0:
        return 100 # PSNR is infinite, set to a high value
    # Maximum possible pixel value (typically 255 for 8-bit images)
    max_pixel = 255.0
    # Calculate PSNR using the formula
    psnr_score = 10 * np.log10(max_pixel ** 2 / mse)
    return psnr_score



def show_res(before_img, after_img):
    """
        Show the original image and the corresponding smooth image
        Inputs:
            before_img: cv2: image before smoothing
            after_img: cv2: corresponding smoothed image
        Return:
            None
    """
    plt.figure(figsize=(12, 9))
    plt.subplot(1, 2, 1)
    plt.imshow(before_img, cmap='gray')
    plt.title('Before')

    plt.subplot(1, 2, 2)
    plt.imshow(after_img, cmap='gray')
    plt.title('After')
    plt.show()


if __name__ == '__main__':
    img_noise = "ex1_images/noise.png" # <- need to specify the path to the noise image
    #img_gt = "" # <- need to specify the path to the gt image
    img = read_img(img_noise)
    filter_size = 3

    # Mean filter
    mean_smoothed_img = mean_filter(img, filter_size)
    show_res(img, mean_smoothed_img)
    print('PSNR score of mean filter: ', psnr(img, mean_smoothed_img))

    # Median filter
    median_smoothed_img = median_filter(img, filter_size)
    show_res(img, median_smoothed_img)
    print('PSNR score of median filter: ', psnr(img, median_smoothed_img))

