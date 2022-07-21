clc
clear
a=imread("untitled.tif")
% whos              %查看图片属性
imshow(a)         %显示变量a;
writematrix(a,'haha.csv')
% b=rgb2gray(a)     %变量a变为2rgb值的灰度图像
% imshow(b)         %显示变量b
% c=im2bw(a)        %把灰度图像转换成二值图像
% imshow(c)         %显示变量c