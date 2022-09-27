import cv2

def crop_square(img, size, interpolation=cv2.INTER_AREA):
    h, w = img.shape[:2]
    min_size = np.amin([h,w])

    # Centralize and crop
    crop_img = img[int(h/2-min_size/2):int(h/2+min_size/2), int(w/2-min_size/2):int(w/2+min_size/2)]
    resized = cv2.resize(crop_img, (size, size), interpolation=interpolation)

    return resized
    

img = cv2.imread("./data/Unsplit Input Data/Yadu/frame0.jpg")
print(img)
cv2.imshow(img)
img2 = crop_square(img, 256)
print(img2.shape)
cv2.imshow(img2)
