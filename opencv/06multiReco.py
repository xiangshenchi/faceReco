#导入cv模块
import cv2 as cv

def face_detect_demo():
    #转换灰度
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #加载分类器（已经训练好，opencv自带）
    face_detect=cv.CascadeClassifier('C:/Users/HP/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    #1:放入的图像 2:缩放倍数 3:确认次数 4:默认为0 5:最小框选尺寸 6:最大框选尺寸
    face = face_detect.detectMultiScale(gray)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img)


#读取图像
img = cv.imread("multiFaces.jpg")
#检测函数
face_detect_demo()
#等待
cv.waitKey(0)
# while True:
#     if ord('q')==cv.waitKey(0):
#         break
#释放内存
cv.destroyAllWindow()