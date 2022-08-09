"""
Preprocessing neuroimages using keras package

@author: Luciamb
"""

import skimage.transform as transf
import matplotlib.pyplot as plt

from load_data import scan_data

#print(scan_data)

# to resize the image we state what size we want it to be
desired_size=(128,128,64)
resized_scan = transf.resize(scan_data, desired_size, order=1, preserve_range=True)
#plt.imshow(resized_scan[:,:,50])
#plt.title('Scan from patient 8, z=50, resized')


# we normalise the image dividing by 255 (since colours go from 0 to 256)
normal_scan = resized_scan/255
#plt.imshow(normal_scan[:,:,50])
#plt.title('Scan from patient 8, z=50, normalised')


# we can rotate the image (anticlockwise) by selecting the degrees
rotate_scan=transf.rotate(scan_data,45)
plt.imshow(rotate_scan[:,:,50])
plt.title('Scan from patient 8, z=50, rotated 45deg')

