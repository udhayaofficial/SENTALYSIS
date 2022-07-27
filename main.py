
import pytesseract
from textblob import TextBlob
import cv2
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract'
img = cv2.imread('d.jpeg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
a=pytesseract.image_to_string(img)
print(pytesseract.image_to_boxes(img))


hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    print(b)
    b=b.split(' ')
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)
    cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)


edu=TextBlob(a)
x=edu.sentiment.polarity
if "Internship" in a:
    x=x+0.3
elif "Intern" in a:
    x=x+0.3
elif "Internships" in a:
    x=x+0.4
elif "Work Experience" in a:
    x=x+0.5
else:
    x=x-1
if x<0:
     print("Poor Resume")
elif x==0:
     print("Average Resume")
elif x>0:
     print("Good Resume")

cv2.imshow('Result',img)
cv2.waitKey(0)
