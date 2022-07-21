
from PIL import Image
import numpy as np
import csv

def standard():
    standard_data = 1
    L_image=Image.open('1.tif')
    img=np.array(L_image)
    print(img.shape)
    imgdata_g = img[:,:,1]
    with open('data1_g.csv', 'w', encoding='utf-8', newline='') as file_obj:
    # 创建对象
        writer = csv.writer(file_obj)
        # 遍历，将每一行的数据写入csv
        for p in imgdata_g:
            writer.writerow(p)
    return standard_data


if __name__ == "__main__":
    L_path='HDV.tif'
    L_image=Image.open(L_path)
    out = L_image.convert("RGB")
    # print(L_image)
    img=np.array(out)
    # img2=np.array(L_image)
    # print(img2.shape)#高 宽 三原色分为三个二维矩阵
    # print(img[0][0])
    # L_image.show()
    # print(type(img))
    # print(out.size)
    # print(img.shape)#高 宽 三原色分为三个二维矩阵

    # print(img[1])
    # np.save('data',np.split(img, 3)[0])

    # im =np.split(img, 4)[0]
    # print(im.shape)
    # i=0
    # while i<6:
    #     for u in img[i]:
    #         print(u[1])
    # i=i+1
    imgdata_g = img[:,:,1]
    print(imgdata_g.shape)
    with open('data_g.csv', 'w', encoding='utf-8', newline='') as file_obj:
    # 创建对象
        writer = csv.writer(file_obj)
        # 遍历，将每一行的数据写入csv
        for p in imgdata_g:
            writer.writerow(p)

    # with open('data.csv', 'w', encoding='utf-8', newline='') as file_obj:
    # # 创建对象
    #     writer = csv.writer(file_obj)
    #     # 遍历，将每一行的数据写入csv
    #     for p in img:
    #         writer.writerow(p)


# new_img = Image.fromarray(im)
# new_img.show()
# new_img.save("new_1.jpg")


    # print(img)
