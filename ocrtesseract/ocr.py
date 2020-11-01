import pytesseract
import cv2

#pip install pytesseract
#pip install opencv-python

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'

img = cv2.imread('test.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))  # To fetch text from image


### Detecting Characters
'''
hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    # print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,hImg-y), (w, hImg-h), (0,0,255), 1) # To Detect the character & put a rectangle around it
    cv2.putText(img,b[0],(x,hImg-y+20), cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1) # To put the Detected text_character around the rectangle.
'''


### Detecting Words
'''hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_data(img)
# print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        # print(b)
        if len(b)==12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y), (w+x, h+y), (0,0,255), 1) # To Detect the character & put a rectangle around it
            cv2.putText(img,b[11],(x,y), cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1) # To put the Detected text_character around the rectangle.
'''

### Detecting Numbers
hImg,wImg,_ = img.shape
cong = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img, config=cong)
# print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        # print(b)
        if len(b)==12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y), (w+x, h+y), (0,0,255), 1) # To Detect the character & put a rectangle around it
            cv2.putText(img,b[11],(x,y), cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1) # To put the Detected text_character around the rectangle.

cv2.imshow('result', img)
cv2.waitKey(0)

