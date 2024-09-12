#导入cv模块
import cv2 as cv
#读取图片
img = cv.imread("face2.jpg")

#修改尺寸
resize_img=cv.resize(img, dsize=(200,200))
#显示原图
cv.imshow("sizeOrigin",img)
#显示修改图
cv.imshow("sizeChanged",resize_img)
#打印原图尺寸
print('未修改',img.shape)
#打印修改尺寸
print('修改后',resize_img.shape)


#等待
while True:
    if ord('q')==cv.waitKey(0):
        break
#释放内存
cv.destroyAllWindow()