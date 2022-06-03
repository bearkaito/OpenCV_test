import imghdr
import cv2

#画像読み込み
img = cv2.imread('yorkie.png', cv2.IMREAD_COLOR)

#ROIで画像を切り出し
img_roi = img[135:320, 150:290]

#画像表示
cv2.imshow('img', img)
cv2.imshow('img_roi', img_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()