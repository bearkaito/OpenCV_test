import cv2

#画像読み込み
src = cv2.imread('yorkie.png', cv2.IMREAD_COLOR)

#x軸を中心に反転
dst = cv2.flip(src, 0)
dst2 = cv2.flip(dst, 0)

#画像表示
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()