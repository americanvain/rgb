
import sys
from traceback import print_tb
import cv2 as cv
import numpy as np
import os

from sqlalchemy import case

#图片路径
#（应避免有中文）
image_path=r'/home/zxf/rgb/standard/1.tif'


#读取图片
#类型：numpy.ndarray
image=cv.imread(image_path)

#显示原图
# cv.imshow('cat',image)


#原图转为灰度图
image_gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
#显示灰度图
# cv.imshow('cat_gray',image_gray)


#OpenCV:threshold
#THRESH_BINARY:大于thresh变maxval，小于等于thresh变0
#THRESH_BINARY_INV:大于thresh变0，小于等于thresh变maxval
#THRESH_TRUNC:大于thresh变thresh，小于等于thresh不变
#THRESH_TOZERO:大于thresh不变，小于等于thresh置0
#THRESH_TOZERO_INV:大于thresh置0，小于等于thresh不变
ret,image_thresh_binary=cv.threshold(image_gray,128,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
#返回值：
#ret：与参数thresh一致
#结果图像
saveFile = "/home/zxf/rgb/standard/process/imgSave.tif"  # 保存文件的路径
# cv2.imwrite(saveFile, img3, [int(cv2.IMWRITE_PNG_COMPRESSION), 8])  # 保存图像文件, 设置压缩比为 8
cv.imwrite(saveFile, image_thresh_binary)  # 保存图像文件
contours, hierarchy = cv.findContours(image_thresh_binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print(contours)
cnt = contours[1]
print(cnt.shape)
list_a = cnt.tolist()
# print(cnt)
cnt2 = cnt[:,:,1]
# print(cnt2)
# 求最大值的索引
# print(np.argmax(cnt2))
# 求最大值
height1 = cnt2[np.argmax(cnt2)][0]-3
height2 = cnt2[np.argmin(cnt2)][0]+3
cnt3 = cnt[:,:,0]
weight1 = cnt3[np.argmax(cnt3)][0]-3
weight2 = cnt3[np.argmin(cnt3)][0]+3
# print(type(height1[0]))
newimage = image[height2:height1,weight2:weight1]

saveFile = "/home/zxf/rgb/standard/process/caijian.tif"  # 保存文件的路径
cv.imwrite(saveFile, newimage)  # 保存图像文件

# M = cv.moments(cnt)
# print(M)
# cx = int(M['m10']/M['m00'])
# cy = int(M['m01']/M['m00'])
# print(cx,cy )

img = cv.drawContours(image, contours, 1, (0,255,0), 1)
# cv.imshow('drawimg',img)
saveFile = "/home/zxf/rgb/standard/process/drawimgSave.tif"  # 保存文件的路径
# cv.imwrite(saveFile, img)  # 保存图像文件

# #显示二值化图片
# cv.imshow('cat_thresh_binary',image_thresh_binary)


# #将灰度图片进行另一种二值化
# ret,image_thresh_binary_inv=cv.threshold(image_gray,128,255,cv.THRESH_BINARY_INV)
# #显示另一种二值化的图片
# cv.imshow('cat_thresh_binary_inv',image_thresh_binary_inv)

cv.waitKey(0)
cv.destroyAllWindows()

