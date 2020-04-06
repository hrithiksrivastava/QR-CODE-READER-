
import cv2
#import numpy as np
import pyzbar.pyzbar as pyzbar
font=cv2.FONT_HERSHEY_PLAIN


#the reading of the data in the image
"""
img= cv2.imread("/home/hrithik/Desktop/qrcode.png")

decode=pyzbar.decode(img)
#print(decode)

for obj in decode:
    print("Data:",obj.data)
    
cv2.imshow("Frame",img)
cv2.waitKey(0)

"""

#to read the QRcode from the web cam
cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    
    decode=pyzbar.decode(frame)
    
    for obj in decode:
        cv2.putText(frame,str(obj.data),(35,50),font,3,(255,255,0),3)
    
    #for obj in decode:
     #   print("Data:",obj.data)
    
    cv2.imshow("Frame",frame)
    
    key=cv2.waitKey(1)
    if key==27:
        break
