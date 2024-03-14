import torch
import torchvision
import torchvision.transforms as T
from PIL import Image
import numpy as np

tensor1 = torch.load('data/images/image_phi-1_theta-1_psi-1_x2709_y-31_h581.pt')
# tensor2 = torch.load('dataWPI_12464/images/image_phi0_theta6_psi-8_x-99_y-55_h377.pt')
tensor3 = torch.load('image_phi-1_theta-1_psi-1_x509_y-31_h466.pt')
tensor4 = torch.load('/home/colette/XPlaneAutolandScenario/dataWPI_12464/images/image_phi-1_theta-1_psi-1_x1809_y-79_h386.pt')



transform = T.ToPILImage(mode = "RGB")

img1 = transform(tensor1)
# img2 = transform(tensor2)
img3 = transform(tensor3)
img4 = transform(tensor4)

rgb_data = np.array(img4)
bgr_data = rgb_data[:, :, ::-1]  # (red,green,blue) --> (blue,green,red)
bgr = Image.fromarray(bgr_data)

img1.show()
# img2.show()
# img3.show()
img4.show()
bgr.show()
