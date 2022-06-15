import numpy as np
import cv2

img = np.array([[1, 2, 3, 4, 5]])

#画像データ中の画素数の最小値を求める
min = img.min()

#最大値を求める
max = img.max()

print(f'min = {min}, max = {max}')


