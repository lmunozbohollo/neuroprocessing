"""
Preprocessing neuroimages using pytorch package

@author: Luciamb
"""

from torchvision import transforms
import matplotlib.pyplot as plt

from load_data import scan_data


"""
 when using PyTorch we must first convert the image to tensor
"""
image_to_tensor = transforms.Compose([transforms.ToTensor()])
scan_in_tensor = image_to_tensor(scan_data)

#print(scan_in_tensor.shape)
#plt.imshow(scan_in_tensor[:,:,50])
#plt.title('Scan in tensor form')


"""
 to rotate the image by the desired number of degrees
"""
random_rotation = transforms.RandomRotation(45)
rotation = transforms.Compose([random_rotation])

scan_rotated = rotation(scan_in_tensor)
#plt.imshow(scan_rotated[:,:,50])
#plt.title('Scan rotated by 45 deg')


"""
 resize the image
"""
resize = transforms.Compose([transforms.Resize(160)])
scan_resized = resize(scan_in_tensor)
#plt.imshow(scan_resized[:,:,50])
#plt.title('Scan resized')


"""
 crop the image
"""
random_cropping = transforms.Compose([transforms.RandomResizedCrop(120)])
scan_cropped = random_cropping(scan_in_tensor)
plt.imshow(scan_cropped[:,:,50])
plt.title('Scan cropped')
print(scan_cropped.shape)

