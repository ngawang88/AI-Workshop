import os
import cv2

path = os.chdir(
    './data/Dataset/Yadu_Nepal')

i = 0
for file in os.listdir(path):

	# img = cv2.imread(file)
	# print(img.shape)
	# dim = (256, 256)
	# # resize image
	# resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	# print(resized.shape)
	i = i + 1
	if i>1500:
		os.remove(file)