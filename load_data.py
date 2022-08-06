"""
Uploading neuroimages for processing

@author: Luciamb
"""

import os


# select folder where the data is stored
path = "FLAIR/"

image = os.listdir(path)

# empty list to add paths to all images
all_images_paths = []

for i in image:
    path=os.path.join(path,i)
    all_images_paths.append(path)
    
print(all_images_paths)