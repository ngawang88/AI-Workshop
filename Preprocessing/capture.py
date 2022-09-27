import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
img_num = 0
total_img = 300
cap_flag = False
path = './Zero'

while(cap.isOpened()):
    # read image
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)

    # get hand data from the rectangle sub window on the screen
    cv.rectangle(frame, (300, 300), (100, 100), (0, 255, 0), 0)

    cv.imshow("image", frame)

    crop_img = frame[100:300, 100:300]

    if cap_flag:
        img_num += 1
        save_img = cv.resize(crop_img, (200, 200))
        save_img = np.array(save_img)
        cv.imwrite(path + "/" + str(img_num) + ".jpg", save_img)
        print('Photo: ', img_num)

    keypress = cv.waitKey(1)

    if img_num == total_img:
        cap_flag = False
        break

    if keypress == ord('q'):
        break
    elif keypress == ord('c'):
        cap_flag = True

cap.release()
cv.destroyAllWindows()
cv.waitKey(1)