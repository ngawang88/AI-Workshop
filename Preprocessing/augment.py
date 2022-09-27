from PIL import Image
import numpy as np
import os
import cv2

Ext = ".jpg"
path = "./Number/Data/Zero"


def invert_image(image, channel, count):
    image = (channel-image)
    cv2.imwrite(path + '/Preprocessed' + "/invert-" +
                str(channel) + str(count) + Ext, image)


def add_light(image, gamma, count):
    inverseGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inverseGamma) *
                      255 for i in np.arange(0, 256)]).astype("uint8")
    image = cv2.LUT(image, table)
    if gamma >= 1:
        cv2.imwrite(path + '/Preprocessed' + "/light-" +
                    str(gamma) + str(count) + Ext, image)
    else:
        cv2.imwrite(path + '/Preprocessed' + "/dark-" +
                    str(gamma) + str(count) + Ext, image)


def add_light_color(image, color, gamma, count):
    inverseGamma = 1.0 / gamma
    image = (color - image)
    table = np.array([((i / 255.0) ** inverseGamma) *
                      255 for i in np.arange(0, 256)]).astype("uint8")
    image = cv2.LUT(image, table)
    if gamma >= 1:
        cv2.imwrite(path + '/Preprocessed' + "/light_color-" +
                    str(gamma) + str(count) + Ext, image)
    else:
        cv2.imwrite(path + '/Preprocessed' + "/dark_color" +
                    str(gamma) + str(count) + Ext, image)


def saturation_image(image, saturation, count):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    v = image[:, :, 2]
    v = np.where(v <= 255 - saturation, v + saturation, 255)
    image[:, :, 2] = v

    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    cv2.imwrite(path + '/Preprocessed' + "/saturation-" +
                str(saturation) + str(count) + Ext, image)


def averageing_blur(image, shift, count):
    image = cv2.blur(image, (shift, shift))
    cv2.imwrite(path + '/Preprocessed' + "/AverageingBLur-" +
                str(shift)+str(count) + Ext, image)


def sharpen_image(image, count):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    image = cv2.filter2D(image, -1, kernel)
    cv2.imwrite(path + '/Preprocessed'+"/Sharpen-"+str(count)+Ext, image)


def grayscale_image(image, count):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path + '/Preprocessed' +
                "/Grayscale-" + str(count) + Ext, image)


def median_blur(image, shift, count):
    image = cv2.medianBlur(image, shift)
    cv2.imwrite(path + '/Preprocessed' + "/MedianBLur-" +
                str(shift)+str(count) + Ext, image)


def multiply_image(image, R, G, B, count):
    image = image*[R, G, B]
    cv2.imwrite(path + '/Preprocessed'+"/Multiply-" +
                str(R)+str(G)+str(B)+str(count)+Ext, image)


def bileteralBlur(image, d, color, space, count):
    image = cv2.bilateralFilter(image, d, color, space)
    cv2.imwrite(path + '/Preprocessed' + "/BileteralBlur-"+str(d) +
                str(color)+str(space) + str(count) + Ext, image)


def erosion_image(image, shift, count):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    cv2.imwrite(path + '/Preprocessed' + "/Erosion-" +
                str(shift)+str(count) + Ext, image)


def dilation_image(image, shift, count):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    cv2.imwrite(path + '/Preprocessed' + "/Dilation-" +
                str(shift)+str(count) + Ext, image)


def morphological_gradient_image(image, shift, count):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    cv2.imwrite(path + '/Preprocessed' + "/Morphological_Gradient-" +
                str(shift)+str(count) + Ext, image)


def top_hat_image(image, shift, count):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    cv2.imwrite(path + '/Preprocessed' + "/Top_Hat-" +
                str(shift)+str(count) + Ext, image)


def black_hat_image(image, shift, count):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
    cv2.imwrite(path + '/Preprocessed' + "/Black_Hat-" +
                str(shift)+str(count) + Ext, image)


def padding_image(image, tBorder, bBorder, lBorder, rBorder, cborder, count):
    image = cv2.copyMakeBorder(image, tBorder, bBorder, lBorder,
                               rBorder, cv2.BORDER_CONSTANT, value=cborder)
    cv2.imwrite(path+'/Preprocessed'+"/padd-"+str(tBorder) +
                str(bBorder)+str(lBorder)+str(rBorder)+str(count)+Ext, image)


imfilelist = [os.path.join(path, f)
              for f in os.listdir(path) if f.endswith(Ext)]

for i, el in enumerate(imfilelist):
    print(i, el)
    image = Image.open(el)
    image = np.array(image)

    invert_image(image, 255, i)
    invert_image(image, 100, i)
    invert_image(image, 50, i)

    add_light(image, 1.5, i)
    add_light(image, 2.5, i)
    add_light(image, 3.0, i)
    add_light(image, 5.0, i)
    add_light(image, 0.7, i)
    add_light(image, 0.4, i)
    add_light(image, 0.1, i)

    add_light_color(image, 255, 1.5, i)
    add_light_color(image, 255, 0.7, i)

    saturation_image(image, 50, i)
    saturation_image(image, 100, i)
    saturation_image(image, 150, i)
    saturation_image(image, 200, i)

    averageing_blur(image, 5, i)
    averageing_blur(image, 4, i)
    averageing_blur(image, 6, i)

    sharpen_image(image, i)

    grayscale_image(image, i)

    median_blur(image, 3, i)
    median_blur(image, 5, i)
    median_blur(image, 7, i)

    multiply_image(image, 0.5, 1, 1, i)
    multiply_image(image, 1, 0.5, 1, i)
    multiply_image(image, 1, 1, 0.5, i)
    multiply_image(image, 0.5, 0.5, 0.5, i)

    bileteralBlur(image, 9, 75, 75, i)
    bileteralBlur(image, 12, 100, 100, i)
    bileteralBlur(image, 25, 100, 100, i)

    erosion_image(image, 1, i)
    erosion_image(image, 3, i)
    erosion_image(image, 6, i)

    dilation_image(image, 1, i)
    dilation_image(image, 3, i)
    dilation_image(image, 5, i)

    morphological_gradient_image(image, 5, i)
    morphological_gradient_image(image, 10, i)
    morphological_gradient_image(image, 15, i)

    top_hat_image(image, 200, i)
    top_hat_image(image, 300, i)
    top_hat_image(image, 500, i)

    black_hat_image(image, 200, i)
    black_hat_image(image, 300, i)
    black_hat_image(image, 500, i)

    padding_image(image, 100, 0, 0, 0, 0, i) 
    padding_image(image, 0, 100, 0, 0, 0, i)
    padding_image(image, 0, 0, 100, 0, 0, i)
    padding_image(image, 0, 0, 0, 100, 0, i)
    padding_image(image, 100, 100, 100, 0, 100, i)