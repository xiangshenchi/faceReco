import os
import cv2
from PIL import Image
import numpy as np


def getImageAndLabels(path):
    # 储存人脸数据
    facesSamples = []
    # 储存姓名数据
    ids = []
    # 储存图片信息
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # 加载分类器
    face_detector = cv2.CascadeClassifier(
        'C:/Users/HP/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    # 遍历列表图片
    for imagePath in imagePaths:
        # 打开图片并灰度化   PIL有9种不同模式：1、L、P、RGB、RGBA、CMYK、YCbCr、T、F。
        # 1:黑白（RGB: 0 or 1） L:灰度（RGB: 0~255）
        PIL_img = Image.open(imagePath).convert('L')
        # 将图像转为数组，以黑白深浅
        img_numpy = np.array(PIL_img, 'uint8')
        # 获取图片人脸特征
        faces = face_detector.detectMultiScale(img_numpy)
        # 获取每张图片的id和姓名
        id = int(os.path.split(imagePath)[1].split('.')[0])
        # 预防无面容图片
        for x, y, w, h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y + h, x:x + w])
            # 打印脸部特征和id
    print('id:', id)
    print('fs:', facesSamples)
    return facesSamples, ids


if __name__ == '__main__':
    # 图片路径
    path = './data/picSave/'
    # 获取 图像数组、id标签数组、姓名
    faces, ids = getImageAndLabels(path)
    # 加载识别器
    recognizer = cv2.face.LBPHFaceRecognizer.create()
    # 训练
    recognizer.train(faces, np.array(ids))
    # 保存文件
    recognizer.write('./trainer/01trainer.yml')
