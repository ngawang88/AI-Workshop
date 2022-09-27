import cv2 
import os

name = 1519

def getFrame(sec): 
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000) 
        hasFrames,image = vidcap.read() 
        if hasFrames: 
            cv2.imwrite("./data/Thimphu/"+str(name)+".jpg", image)     # save frame as JPG file 
        return hasFrames 

for file in os.listdir("Z:/Notes/7th sem/CTE411 - Artificial Intelligence (Elective II)/Mini Project/Dataset/FruitsVeg_Videos/Phuentsholing/"):
    vidcap = cv2.VideoCapture("Z:/Notes/7th sem/CTE411 - Artificial Intelligence (Elective II)/Mini Project/Dataset/FruitsVeg_Videos/Phuentsholing/"+file)
    sec = 0 
    frameRate = 0.5 # it will capture image in each 0.5 second 
    success = getFrame(sec) 
    while success: 
        name= name+1
        sec = sec + frameRate 
        sec = round(sec, 2) 
        success = getFrame(sec) 