
import imp
from PIL import Image
import numpy as np
import csv
import os
import cv2 as cv
standard_data = 1
img = cv.imread('messi5.jpg')
print(img)
L_image=Image.open('1.tif')
L_image = L_image.convert("RGB")
# L_image2 = L_image.convert("L")
# L_image2.show()

# path = '/home/zxf/rgb/standard'
# dir1 = os.listdir(path)
# for image_standard in dir1:
#     L_image=Image.open(image_standard)

img=np.array(L_image)
# print(L_image)
imgdata_g = img[:,:,0]
# # imgdata_g = img

new_img = Image.fromarray(imgdata_g)
# new_img.show()
new_img.save("new_1.jpg")
print(new_img)


# with open('data1_g.csv', 'w', encoding='utf-8', newline='') as file_obj:
# # 创建对象
#     writer = csv.writer(file_obj)
#     # 遍历，将每一行的数据写入csv
#     for p in imgdata_g:
#         writer.writerow(p)