import cv2
from cv2 import hconcat

img1 = cv2.imread('yorkie.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('yorkie_flip_0.png', cv2.IMREAD_COLOR)

hconcat_img = cv2.hconcat([img1, img2])

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('hconcat_img', hconcat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()