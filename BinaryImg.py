import numpy as np
from PIL import Image

gray_img = Image.open('camera7.bmp').convert("LA")#밝기와 알파값을 이용해 그레이스케일로 전환
gray_img.show()

row = gray_img.size[0]
col = gray_img.size[1]
thr_img = Image.new("1",(row,col)) # new binary image

for x in range(1,row):
    for y in range(1,col):
        if gray_img.getpixel((x,y))[0] > 128:#rgb 전부 같음 따라서 임계값과 비교
            thr_img.putpixel((x,y),0)
        else:
            thr_img.putpixel((x,y),1)
thr_img.show()