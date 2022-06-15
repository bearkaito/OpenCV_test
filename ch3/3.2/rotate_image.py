import cv2
from cv2 import rotate

#画像読み込み
src = cv2.imread('yorkie.png', cv2.IMREAD_COLOR)

#画像90度回転
rotate = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)

#画像をウィンドウ表示
cv2.imshow('src', src)
cv2.imshow('rotate', rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()