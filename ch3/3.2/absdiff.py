import numpy as np
import cv2

img1 = np.array([[1, 2, 3, 4, 5]])
img2 = np.array([[5, 4, 3, 2, 1]])

#ピクセルごとの差分の絶対値
diff = cv2.absdiff(img1, img2)

#1-5=4
#2-4
#3-3
#4-2
#5-1

print(diff)