clc
clear
image = imread("20210515231219627.png");
R = image(:,:,1);  %  提取R值的矩阵
G = image(:,:,2);  %  提取G值的矩阵
B = image(:,:,3);  %  提取B值的矩阵
ranks_R = size(R);  %  提取图片的像素（一个m×n的矩阵）
result = cell(ranks_R(1), ranks_R(2));  %  创建一个 m×n 的空cell矩阵
 
%  提取像素的行列数，将R、G、B对应的值组成一个 1×3 的矩阵
 
for row = 1:ranks_R(1)
    for column = 1:ranks_R(2)
        row_column_R = R(row, column);
        row_column_G = G(row, column);
        row_column_B = B(row, column);
        mat = mat2str([row_column_R row_column_G row_column_B]); % 将RGB矩阵转换成字符串，以便存入cell
        result{row, column} = mat;  %  将每一个像素值分别存入result
    end
end
writecell(result,'result.xlsx')