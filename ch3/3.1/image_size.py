import imghdr
import cv2

#画像をカラーで読み込み
img = cv2.imread('yorkie.png' ,cv2.IMREAD_COLOR)

if len(img.shape) == 3:
    #カラー画像
    height, width, channels = img.shape[:3]
else:
    #グレー画像
    height, width = img.shape[:2]
    channels = 1
    
#width, height, channels を表示
print(f'width = {width}')
print(f'height = {height}')
print(f'channels = {channels}')
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
