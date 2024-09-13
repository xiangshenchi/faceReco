# 导入模块
import cv2 as cv

# 调用摄像头
cap = cv.VideoCapture(0)

flag = 1
num = 1

while (cap.isOpened()):  # 检测摄像头是否开启
    ret_flag, Vshow = cap.read()  # 得到每帧图像
    cv.imshow("Capture_test", Vshow)
    k = cv.waitKey(1) & 0xFF  # 按键判断
    if k == ord('s'):
        cv.imwrite("./data/picSave/" + str(num) + ".xsc" + ".jpg", Vshow)
        print('Success to save img: ' + str(num) + ".jpg")
        print('--------------------------------------')
        num += 1
    elif k == ord('q'):  # 退出
        break
# 释放摄像头
cap.release()
# 释放内存
cv.destroyAllWindows()
