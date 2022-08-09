"""
Preprocessing neuroimages using keras package

@author: Luciamb
"""

import skimage.transform as transf
import matplotlib.pyplot as plt
import numpy as np
import random

from load_data import scan_data

from skimage.restoration import denoise_nl_means


"""
 to resize the image we state what size we want it to be
"""
desired_size=(128,128,64)
resized_scan = transf.resize(scan_data, desired_size, order=1, preserve_range=True)
#plt.imshow(resized_scan[:,:,50])
#plt.title('Scan from patient 8, z=50, resized')


"""
 we normalise the image dividing by 255 (since colours go from 0 to 256)
"""
normal_scan = resized_scan/255
#plt.imshow(normal_scan[:,:,50])
#plt.title('Scan from patient 8, z=50, normalised')


"""
 we can rotate the image (anticlockwise) by selecting the degrees
"""
rotate_scan=transf.rotate(scan_data,45)
#plt.imshow(rotate_scan[:,:,50])
#plt.title('Scan from patient 8, z=50, rotated 45deg')


"""
 add noise using gaussian noise to prevent overfitting
"""
def gauss_noise(sample ,noise_var):
    
    if noise_var[0] == noise_var[1]:
        variance = noise_var[0]
    else:
        variance = random.uniform(noise_var[0], noise_var[1])
    sample = sample + np.random.normal(0.0, variance, size=sample.shape)
    return sample

noise_var = (0, 1)
noisy_scan = gauss_noise(normal_scan,noise_var)
#plt.imshow(noisy_scan[:,:,50])
#plt.title('Scan from patient 8, z=50, with noise')


"""
 denoising using non local means
"""
denoised_scan=denoise_nl_means(noisy_scan, 7, 5, 0.01, fast_mode=True,sigma=0.6)
plt.imshow(denoised_scan[:,:,50])
plt.title('Scan from patient 8, z=50, denoised')
