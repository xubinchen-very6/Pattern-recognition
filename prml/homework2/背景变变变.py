import numpy as np
import cv2


img = cv2.imread('/Users/macbookair/PycharmProjects/PR/homework2/unpro.jpg')
bg = cv2.imread('/Users/macbookair/PycharmProjects/PR/homework2/back2.png')#---->3750*2500
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (1250,25,2000,2325)
# rect = (1,1,l-2,w-2)
#1250 25 2400 2450

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
mask2 = cv2.erode(mask2,None,iterations=2)
mask2 = cv2.dilate(mask2,None,iterations=1)
mask_inv = np.where((mask2==0),1,0).astype('uint8')

img1 = img*mask2[:,:,np.newaxis]
img2 = bg*mask_inv[:,:,np.newaxis]
dst=cv2.addWeighted(img1,1,img2,1,0)
cv2.imshow('output',dst)
cv2.imwrite('output.jpg',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
