import cv2

#画像ファイルをカラーで読み込み
img = cv2.imread('yorkie.png', cv2.IMREAD_COLOR)

print(f'shape = {img.shape}')
print(f'dtype = {img.dtype}')