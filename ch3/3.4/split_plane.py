import cv2
from cv2 import imread

#画像ファイルを読み込み
img =  cv2.imread('yorkie.png', cv2.IMREAD_ANYCOLOR)

#プレーンの抽出
b_plane, g_plane, r_plane = cv2.split(img)

#画像を表示
cv2.imshow('img', img)
cv2.imshow('r_plane', r_plane)
cv2.imshow('g_plane', g_plane)
cv2.imshow('b_plane', b_plane)
cv2.waitKey(0)
cv2.destroyAllWindows()
