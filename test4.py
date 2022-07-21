
#erwer fdsfd
if __name__ == "__main__":      #定义主函数入口
    num=[]                      #定义一个名为num的列表
    i=2                         #定义被除数，变量名为i
    for i in range(2,100):      #i的取值范围是2-100
        j=2                     #定义除数，变量名为j
        for j in range(2,i):    #j的取值范围是2到当前循环内被除数的值
            if(i%j==0):         #判断是否存在某个除数可以整除被除数，即他们的余数为零
                break           #如果存在，那么该被除数不为素数，结束该循环
        else:
            num.append(i)   #如果不存在，被除数为素数，将其添加进num列表中
    
    print(num)                  #最后打印所有的素数

    pass