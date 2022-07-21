
import cv2 as cv
import numpy as np
import os
import re

path = '/home/zxf/rgb/standard'
save_path = r'/home/zxf/rgb/standard/process'
dir1 = os.listdir(path)

for filelist in dir1:
    print(filelist)
    tmp=re.findall(r"\d.tif$",filelist)
    if tmp==[]:
        continue
    open_path = os.path.join(path,filelist)
    save_path1 = os.path.join(save_path,filelist)
    # print(save_path1)
    image=cv.imread(open_path)
    cv.imshow(filelist,image)
    # 待完成：
    image_gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)



cv.waitKey(0)
cv.destroyAllWindows()











    # save_path_file = os.path.join(save_path,filelist)
    # cv.imwrite(saveFile, newimage)  # 保存图像文件  
