"""
Uploading neuroimages for processing

@author: Luciamb
"""

import nibabel as nib
import matplotlib.pyplot as plt
import PyQt5

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
print(shape)


z_slice = 60
plt.imshow(scan_data[:,:,z_slice]) # select the desired plane and slice on that plane
plt.title('Scan from patient {}, z={}'.format(str(scan_number),z_slice))
plt.show()
# conseguir cambiar x e y tambien