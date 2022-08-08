"""
Uploading neuroimages for processing

@author: Luciamb
"""

import nibabel as nib
import matplotlib.pyplot as plt


# select folder where the data is stored
scan_number = 28
path = "FLAIR/BraTS2021_{}_flair.nii.gz".format(str(scan_number).zfill(5))


# upload the desired scan from the folder
scan = nib.load(path)

# to show scan as matrices
scan_data = scan.get_fdata()
#print(scan_data)


header=scan.header
#print(header)


# to observe how many slices were taken in each direction
shape=scan.shape
#print(shape)


# select the desired plane and slice to view on that plane
plane = input("Which plane do you want to view the slice in (x, y or z)? ")

if plane == 'x':
    x_slice = int(input("Which slice (0 to {}) would you like to observe? ".format(shape[0])))
    plt.imshow(scan_data[x_slice,:,:]) 
    plt.title('Scan from patient {}, x={}'.format(str(scan_number),x_slice))

if plane == 'y':
    y_slice = int(input("Which slice (0 to {}) would you like to observe? ".format(shape[1])))
    plt.imshow(scan_data[:,y_slice,:]) 
    plt.title('Scan from patient {}, y={}'.format(str(scan_number),y_slice))
    
if plane == 'z':
    z_slice = int(input("Which slice (0 to {}) would you like to observe? ".format(shape[2])))
    plt.imshow(scan_data[:,:,z_slice]) 
    plt.title('Scan from patient {}, z={}'.format(str(scan_number),z_slice))

else:
    print("Sorry, that was not an option.")

plt.show()
