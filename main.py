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
pathImages = sorted(os.listdir(folderPath))

imgNumber =0
hs , ws = int(120*1),int(213*1)
gestureThreshHold = 300
buttonPressed = False
buttonCounter=0
buttonDelay = 10
annotations = [[]]
annotationNumber = 0
annotationStart = False

# --- New Features Variables ---
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255)]
colorNames = ["Red", "Green", "Blue", "Yellow"]
colorIndex = 0
colorChangePressed = False
colorChangeCounter = 0
colorChangeDelay = 15
annotationColors = [colors[colorIndex]]

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

        # Slide Navigation (Static Gestures)
        if cy <= gestureThreshHold:
            annotationStart = False
            # Previous Slide - Thumb Up
            if fingers == [1, 0, 0, 0, 0]:
                print('Previous Slide')
                if imgNumber > 0:
                    imgNumber -= 1
                    annotations = [[]]
                    annotationColors = [colors[colorIndex]]
                    annotationNumber = 0
                    buttonPressed = True
            
            # Next Slide - Pinky Up
            if fingers == [0, 0, 0, 0, 1]:
                print('Next Slide')
                if imgNumber < len(pathImages) - 1:
                    imgNumber += 1
                    annotations = [[]]
                    annotationColors = [colors[colorIndex]]
                    annotationNumber = 0
                    buttonPressed = True
        # COLOR CHANGE - thumb + pinky
        if fingers == [1, 0, 0, 0, 1] and not colorChangePressed:
            annotationStart = False
            colorIndex = (colorIndex + 1) % len(colors)
            colorChangePressed = True

        # draw a circle hilight - show pointer
        if fingers == [0,1,1,0,0]:
            cv2.circle(imgCurrent, indexFinger,12,colors[colorIndex],cv2.FILLED)
            annotationStart = False

        # Draw line using pointer
        if fingers == [0,1,0,0,0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber += 1
                annotations.append([])
                annotationColors.append(colors[colorIndex])
            cv2.circle(imgCurrent, indexFinger,12,colors[colorIndex],cv2.FILLED)
            annotations[annotationNumber].append(indexFinger)
        else:
            annotationStart = False

        # remove drawed line
        if fingers == [0,1,1,1,0]:
            if annotations:
                if annotationNumber >= 0:
                    annotations.pop(-1)
                    if len(annotationColors) > 1:
                        annotationColors.pop(-1)
                    annotationNumber -=1
                    buttonPressed = True
    else :
        annotationStart = False

    if buttonPressed is True:
        buttonCounter +=1
        if buttonCounter >buttonDelay:
            buttonCounter = 0
            buttonPressed = False

    if colorChangePressed:
        colorChangeCounter += 1
        if colorChangeCounter > colorChangeDelay:
            colorChangeCounter = 0
            colorChangePressed = False

    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                color = annotationColors[i] if i < len(annotationColors) else (0,0,200)
                cv2.line(imgCurrent,annotations[i][j-1],annotations[i][j],color,10)

    # Slide count overlay
    h, w, _ = imgCurrent.shape
    if len(pathImages) > 0:
        slideText = f"{imgNumber + 1} / {len(pathImages)}"
        textSize = cv2.getTextSize(slideText, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
        textX = w - textSize[0] - 20
        textY = h - 20

        overlay = imgCurrent.copy()
        cv2.rectangle(overlay, (textX - 10, textY - textSize[1] - 10),
                      (textX + textSize[0] + 10, textY + 10), (0, 0, 0), cv2.FILLED)
        imgCurrent = cv2.addWeighted(overlay, 0.6, imgCurrent, 0.4, 0)
        cv2.putText(imgCurrent, slideText, (textX, textY),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Color indicator
    cv2.rectangle(imgCurrent, (10, h - 50), (50, h - 10), colors[colorIndex], cv2.FILLED)
    cv2.putText(imgCurrent, colorNames[colorIndex], (60, h - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    imgSmall = cv2.resize(image,(ws,hs))
    imgCurrent[0:hs,w-ws:w] = imgSmall
    
    cv2.imshow('image',image)
    cv2.imshow('Slides', imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break