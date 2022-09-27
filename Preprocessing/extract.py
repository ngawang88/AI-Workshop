# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("Z:/Notes/7th sem/CTE411 - Artificial Intelligence (Elective II)/Mini Project/Dataset/FruitsVeg_Videos/Paro/VID_20220703_085612.mp4")

try:
	
	# creating a folder named data
	if not os.path.exists('data/Paro'):
		os.makedirs('data/Paro')

# if not created then raise error
except OSError:
	print ('Error: Creating directory of data')

# frame
currentframe = 0

while(True):
	
	# reading from frame
	ret,frame = cam.read()

	if ret:
		# if video is still left continue creating images
		name = './data/Paro' + str(currentframe) + '.jpg'
		print ('Creating...' + name)

		# writing the extracted images
		
		print('Original Dimensions : ',frame.shape)

		scale_percent = 25 # percent of original size
		width = int(frame.shape[1] * scale_percent / 100)
		height = int(frame.shape[0] * scale_percent / 100)

		dim = (width, height)

		# resize image
		resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
		print(resized.shape)
		cv2.imwrite(name, resized)

		# increasing counter so that it will
		# show how many frames are created
		currentframe += 1

		
	else:
		break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
