import cv2
import numpy as np

img = cv2.imread('/Users/macbookair/PycharmProjects/PR/homework3/input.png',0)
max=np.max(img)
min=np.min(img)
mean = np.mean(img)

for i in img:
    for ji,j in enumerate(i):
        if ji>=338:
            i[ji]+=1

img = (img-min)*((255/((max-min)+10)))



img = cv2.GaussianBlur(img,(7,7),3)

x = cv2.Sobel(img,cv2.CV_16S,1,0,ksize=5)
y = cv2.Sobel(img,cv2.CV_16S,0,1,ksize=5)

x_abs = cv2.convertScaleAbs(x)
y_abs = cv2.convertScaleAbs(y)


cv2.imshow('sobelx',x_abs)
cv2.imshow('sobely',y_abs)

img = cv2.addWeighted(x_abs,0.75,y_abs,0.8,0)

img= np.where(img<62,0,img).astype('uint8')
img = cv2.medianBlur(img,9)
img = cv2.medianBlur(img,9)

img = cv2.applyColorMap(img,cv2.COLORMAP_SUMMER)
# img = cv2.dilate(img,None,iterations=2)
# img = cv2.erode(img,None,iterations=2)
# img = cv2.erode(img,None,iterations=2)
# img = cv2.dilate(img,None,iterations=1)
img = cv2.erode(img,None,iterations=1)
img = cv2.dilate(img,None,iterations=2)
img = cv2.dilate(img,None,iterations=2)
img = cv2.erode(img,None,iterations=2)
img = cv2.erode(img,None,iterations=1)
img = cv2.erode(img,None,iterations=1)
img = cv2.erode(img,None,iterations=1)




cv2.imshow('img',img)
cv2.imwrite('output.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

