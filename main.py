import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np

folderPath = "presentataion"
width = 1280
height = 720

# Camara setup
cap=cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

# Get te List of Slides
pathImages = sorted(os.listdir(folderPath),key=len)

imgNumber =0
hs , ws = int(120*1),int(213*1)
gestureThreshHold = 300
buttonPressed = False
buttonCounter=0
buttonDelay = 10
annotations = [[]]
annotationNumber = 0
annotationStart = False

detector = HandDetector(detectionCon=0.8 , maxHands=1)
while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)

    pathFullImage = os.path.join(folderPath,pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands,img = detector.findHands(image)
    cv2.line(image , (0,gestureThreshHold),(width,gestureThreshHold),(0,255,0),10)

    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        # print(fingers)

        cx,cy = hand['center']
        lmList = hand['lmList']


        xVal = int(np.interp(lmList[8][0],[width // 2,width], [0,width]))
        yVal = int(np.interp(lmList[8][1],[150, height-150], [0,height]))
        indexFinger = xVal,yVal

        if cy <= gestureThreshHold:
            annotationStart = False
            # change to previous slide
            if fingers == [1,0,0,0,0]:
                print('Left');
                annotationStart = False
                if imgNumber > 0:
                    annotations = [[]]
                    annotationNumber = 0
                    buttonPressed = True
                    imgNumber -= 1
            # change to next slide
            if fingers == [0,0,0,0,1]:
                annotationStart = False
                print('Right');
                if imgNumber < len(pathImages)-1:
                    annotations = [[]]
                    annotationNumber = 0
                    buttonPressed = True
                    imgNumber += 1

        # draw a circle hilight - show pointer
        if fingers == [0,1,1,0,0]:
            cv2.circle(imgCurrent, indexFinger,12,(0,0,255),cv2.FILLED)
            annotationStart = False

        # Draw line using pointer
        if fingers == [0,1,0,0,0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber += 1
                annotations.append([])
            cv2.circle(imgCurrent, indexFinger,12,(0,0,255),cv2.FILLED)
            annotations[annotationNumber].append(indexFinger)
        else:
            annotationStart = False

        # remove drawed line
        if fingers == [0,1,1,1,0]:
            if annotations:
                if annotationNumber >= 0:
                    annotations.pop(-1)
                    annotationNumber -=1
                    buttonPressed = True
    else :
        annotationStart = False

    if buttonPressed is True:
        buttonCounter +=1
        if buttonCounter >buttonDelay:
            buttonCounter = 0
            buttonPressed = False

    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(imgCurrent,annotations[i][j-1],annotations[i][j],(0,0,200),10)

    imgSmall = cv2.resize(image,(ws,hs))
    h,w,c = imgCurrent.shape
    imgCurrent[0:hs,w-ws:w] = imgSmall
    
    cv2.imshow('image',image)
    cv2.imshow('Slides', imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break