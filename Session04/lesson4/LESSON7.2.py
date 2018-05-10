import cv2
import numpy as np
import win32com.client


def detectMove(cx, cy, frame,flag):
    # draw reference
    cv2.rectangle(frame, (150,150), (300,300), (0, 0, 255),5)
    cv2.circle(frame, (225,225), 10, [0, 0, 255], 5)
    if (cx-255)>100:
        if flag ==0:
            print("Turn left")
            flag =1
    if (cx -255)<-75:
        if flag ==0:
            print("Turn right")
            flag=1
    if (cx-225)>-75:
        if (cx-225)<100:
            print("Stay")
            flag=0
    cv2.imshow("contour", frame)
    return flag


def findContourMax(image, frame):
    #find contour
    bin, contours,hierachy = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.RETR_TREE)
    contour_max_area = 0
    index_max = 0
    for i in range(len(contours)):

        contours_i = contours[i]
        area_i = cv2.contourArea(contours_i)

        if (area_i>contour_max_area):
            contour_max_area = area_i
            index_max = i

        cv2.drawContours(frame, contours,i,[0,255,0])
    M = cv2.moments(contours[index_max])
    cx = int(M["m10"]/M["m00"])
    cy = int(M["m01"]/M["m00"])
    cv2.circle(frame,(cx,cy),10,[0,255,255])
    cv2.drawContours(frame, contours,index_max,[0,255,0],5)
    return (cx,cy)

    cv2.imshow("contour",frame)

# Create capture from video
cap = cv2.VideoCapture(0)

# Threshold for binary
lower = np.array([60,25,30], dtype = 'uint8')
upper = np.array([255,220,255], dtype = 'uint8')
flag = 0
while True:
    _,frame = cap.read()
    #hàm cap.read sẽ trả về 2 cái (1 cái là có đọc được hay không, 1 cái là frame (nếu ko quan tâm đến 1 biến số nào đó thì sẽ dùng Shiff (-_

    #conver frame HSV
    framehsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(framehsv,lower,upper)
    ker = cv2.getStructuringElement(cv2.MORPH_ERODE, (5, 5))
    newmask = cv2.erode(mask, ker)
    newmask1 =  cv2.dilate(newmask, ker)
    (cx,cy) = findContourMax(newmask,frame)



    flag = detectMove(cx,cy,frame,flag)
    cv2.imshow('video',newmask)
    k = cv2.waitKey(40)
    if k == ord(' '):
        break

