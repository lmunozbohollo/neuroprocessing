"""
Preprocessing neuroimages using pytorch package

@author: Luciamb
"""

import torch
import torchvision
from torchvision import transforms
import matplotlib.pyplot as plt

from load_data import scan_data


"""
 when using PyTorch we must first convert the image to tensor
"""
image_to_tensor = transforms.Compose([transforms.ToTensor()])
scan_in_tensor = image_to_tensor(scan_data)

print(scan_in_tensor.shape)
plt.imshow(scan_in_tensor[:,:,50])
plt.title('Scan in tensor form')

