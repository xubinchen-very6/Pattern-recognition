import cv2
import numpy as np

def is_inside(o,i):
    ox,oy,ow,oh = o
    ix,iy,iw,ih = i
    return (ox>ix) and (oy>iy) and (ox+ow<ix+iw) and (oy+ oh<iy+ih)

def draw_person(image,person):
    x,y,w,h = person
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)

img = cv2.imread('/Users/macbookair/PycharmProjects/PR/homework2/unpro.jpg')
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

found,w = hog.detectMultiScale(img)
print(found,w)
found_filtered = []
for ri,r in enumerate(found):
    for qi,q in enumerate(found):
        if ri != qi and is_inside(r,q):
            break
    else:
        found_filtered.append(r)
for person in found_filtered:
    draw_person(img,person)

cv2.imshow('dection',img)
cv2.imwrite('output.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()