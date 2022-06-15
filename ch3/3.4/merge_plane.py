import cv2

b_plane = cv2.imread('yorkie_split_blue.png', cv2.IMREAD_GRAYSCALE)
g_plane = cv2.imread('yorkie_split_green.png', cv2.IMREAD_GRAYSCALE)
r_plane = cv2.imread('yorkie_split_red.png', cv2.IMREAD_GRAYSCALE)

#プレーン結合
merged = cv2.merge((b_plane, g_plane, r_plane))

cv2.imshow('r_plane', r_plane)
cv2.imshow('g_plane', g_plane)
cv2.imshow('b_plane', b_plane)
cv2.imshow('merged', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()