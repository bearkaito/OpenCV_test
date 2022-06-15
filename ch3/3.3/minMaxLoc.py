import numpy as np
import cv2

img = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#最大値、最小値を求める
min_val, max_val, min_loc, max_loc =cv2.minMaxLoc(img)

print(f'min_val = {min_val}')
print(f'max_val = {max_val}')
print(f'min_loc = {min_loc}')
print(f'min_loc = {max_loc}')