import cv2
import numpy as np

def detectMove(cx, cy, fram, flag):
    cv2.rectangle(frame, (150, 150), (300,300), (0,0,255), 5)
    cv2.circle(frame, (255, 255), 10, (0,0,255), 5)
    if (cx-255) > 100:
        if flag == 0:
            print("Turn right")
            flag = 1
    if (cx-255) <-75:
        if flag == 0:
            print("Turn left")
            flag = 1
    if (cx-255)>-75:
        if (cx-255) < 100:
            print("Stay")
            flag = 0
    cv2.imshow("contour", frame)
    return flag

def findContourMax(image, frame):
    bin, contours, hierachy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.RETR_TREE)
    contour_max_area = 0
    index_max = 0
    for i in range(len(contours)):
        contours_i = contours[i]
        area_i = cv2.contourArea(contours_i)

        if (area_i > contour_max_area)
