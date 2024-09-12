#导入cv模块
import cv2 as cv

def face_detect_demo(img):
    #转换灰度
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #加载分类器（已经训练好，opencv自带）
    face_detect=cv.CascadeClassifier('C:/Users/HP/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    #1:放入的图像 2:缩放倍数 3:确认次数 4:默认为0 5:最小框选尺寸 6:最大框选尺寸
    face = face_detect.detectMultiScale(gray)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img)


#读取摄像头
cap=cv.VideoCapture(0)  #"0"为默认摄像头

#读取视频
# cap=cv.VideoCapture('video.mp4')

#循环
while True:
    flag, frame =cap.read()
    if not flag:    #flag为空（摄像头无内容）
        break
    face_detect_demo(frame)

    if ord('q')==cv.waitKey(1):
        break
#释放内存
cv.destroyAllWindow()
#释放摄像头
cap.release()