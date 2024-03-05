import numpy as np

"""
we have to add some noise using Gaussian Blur or any other smoothing filter for 2 reasons

1- the original digits which the model was trained on had some noise and 
did not look as perfect as drawn on the pallete

2- the actual digits were thicker than the ones drawn on the pallete

so, the gaussian will basically reduce the gap between the original digits in the 
MNIST dataset and the drawn digits

"""
def gaussian_blur(image):

    ## both are hyperparameters
    kernel_size = 3 
    sigma = 1   

    # padding the image
    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='constant')

    #  creating the kernel
    x = np.arange(-pad_size, pad_size + 1)
    y = np.arange(-pad_size, pad_size + 1)
    xx, yy = np.meshgrid(x, y)
    kernel = np.exp(-(xx**2 + yy**2) / (2.0 * sigma**2))
    kernel /= 2 * np.pi * sigma**2
    kernel /= kernel.sum()

    # convoluting the image with the kernel
    blurred_image = np.zeros_like(image, dtype=np.float64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            blurred_image[i, j] = np.sum(padded_image[i:i+kernel_size, j:j+kernel_size] * kernel)

    return blurred_image.astype(np.uint8)