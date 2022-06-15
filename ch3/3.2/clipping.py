from operator import imod
import numpy as np 
import cv2

img = np.array([[0, 1, 2, 3, 4, 5, 6]])

#1から5の範囲でクリップ
clip1 = img.clip(1, 5)
print(f'clip1 = {clip1}')

#最大値を5として値がクリッピング
clip2 = img.clip(None, 5)
print(f'clip2 ={clip2}')