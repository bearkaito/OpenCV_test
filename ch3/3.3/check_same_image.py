from multiprocessing.sharedctypes import Value
from turtle import width
import numpy as np
import cv2

#画像データの内容が同一かをチェックする
def is_same_image(img1, img2):
    # 差分の絶対値をけいさんする
    diff = cv2.absdiff(img1, img2)
    #画素数が非ゼロの画素数をカウントして、０ならTure,そうでなければfalese
    return (cv2.countNonZero(diff) ==0 )

width = 200
height = 100
value1 = 128
value2 = 255

# img1は画素数として128を持ち、img2は画素数として255を持つ
img1 = np.full((height, width), value1, np.uint8)
img2 = np.full((height, width), value2, np.uint8)

print(is_same_image(img1, img1))

print(is_same_image(img1, img2))
