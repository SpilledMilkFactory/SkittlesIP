"""
11/18/2020
Team #25 EGR-107 Semester Project
Connor Grimberg & Christopher Sutton

Image processing program that detects skittles and their individual colors in .jpg photos on a variety of backgrounds.

Required Installed Libraries: OpenCV, NumPy
Verified & Tested in: Python 3.7 - 3.8.1
Verified Last: 11/18/2020
"""

import sys
import cv2 as cv
import numpy as np
import operator
import time
import math

def color_mask(imgarray, procedure):
    hsv = cv.cvtColor(imgarray, cv.COLOR_BGR2HSV)
    if procedure == 'RED':
        lower_range = np.array([0,60,60], np.uint8)
        upper_range = np.array([3,210,210], np.uint8)
        mask = cv.inRange(hsv, lower_range, upper_range)
        return mask
    if procedure == 'ORANGE':
        lower_range = np.array([6,100,100], np.uint8)
        upper_range = np.array([11,255,255], np.uint8)
        mask = cv.inRange(hsv, lower_range, upper_range)
        return mask
    if procedure == 'YELLOW':
        lower_range = np.array([25,100,100], np.uint8)
        upper_range = np.array([35,255,255], np.uint8)
        mask = cv.inRange(hsv, lower_range, upper_range)
        return mask
    if procedure == 'LIME':
        lower_range = np.array([35,100,100], np.uint8)
        upper_range = np.array([85,255,255], np.uint8)
        mask = cv.inRange(hsv, lower_range, upper_range)
        return mask
    if procedure == 'PURPLE':
        lower_range = np.array([80,0,0], np.uint8)
        upper_range = np.array([255,60,60], np.uint8)
        mask = cv.inRange(hsv, lower_range, upper_range)
        return mask




def main(argv):
    # image = cv.imread('s1.jpg')
    # hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    # lower_range = np.array([0,100,100], np.uint8)
    # upper_range = np.array([5,255,255], np.uint8)
    # mask = cv.inRange(hsv, lower_range, upper_range)

    default_file = 's1.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1


    start = time.time()
    
    cstart = time.time()
    # Converting from BGR to Gray 
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # Applying median blur
    gray = cv.medianBlur(gray, 5)
    rows = gray.shape[0]
    # Applying Circle Hough Transform


    #standard 4000x3000
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 175,
                               param1=80, param2=25,        #80, 25
                               minRadius=80, maxRadius=150)
    #resized 1500x1100
    # circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 65,
    #                            param1=80, param2=25,
    #                            minRadius=20, maxRadius=70)


    
    print("Circle Detection done in: " + str(time.time() - cstart))

    colorstart = time.time()


    ccountdict = {
    "red": 0,
    "orange": 0,
    "yellow": 0,
    "lime": 0,
    "purple": 0
    }

    cvaluedict = {
    "red": (0, 0, 255),
    "orange": (0, 128, 255),
    "yellow": (0, 255, 255),
    "lime": (0, 255, 0),
    "purple": (255, 0, 200)
    }

    if circles is not None:
        rmask = color_mask(src, 'RED')
        omask = color_mask(src, 'ORANGE')
        ymask = color_mask(src, 'YELLOW')
        lmask = color_mask(src, 'LIME')
        pmask = color_mask(src, 'PURPLE')

    
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            radius = i[2]
            colordict = {
            "red": 0,
            "orange": 0,
            "yellow": 0,
            "lime": 0,
            "purple": 0
            }
            h = i[0]
            k = i[1]
            rad = i[2]
            for x in range(h - rad, h + rad + 1):
                #print(x)
                for y in range(k - rad, k + rad + 1):
                    if (x - h) * (x - h) + (y - k) * (y - k) <= rad * rad and x >= 0 and y >= 0 and y < src.shape[0] and x < src.shape[1]:
                        if rmask[y, x] == 255:
                            colordict["red"] += 1
                        if omask[y, x] == 255:
                            colordict["orange"] += 1
                        if ymask[y, x] == 255:
                            colordict["yellow"] += 1
                        if lmask[y, x] == 255:
                            colordict["lime"] += 1
                        if pmask[y, x] == 255:
                            colordict["purple"] += 1
            
            # if max(colordict, key=colordict.get) == "yellow":
            #     print(colordict[max(colordict, key=colordict.get)]/(math.pi * rad * rad))

            percentage = colordict[max(colordict, key=colordict.get)]/(math.pi * rad * rad)
            if percentage >= .05: # and percentage <= .7:
                ccountdict[max(colordict, key=colordict.get)] += 1
                cv.circle(src, center, radius, cvaluedict[max(colordict, key=colordict.get)], 3)#TODO differentiate color and swap (,,,) for color var
    

    print("Color Detection done in: " + str(time.time() - colorstart))
    print("Time taken: " + str(time.time() - start))
    print(ccountdict)

    # cv.namedWindow("masks", cv.WINDOW_NORMAL)
    # cv.imshow("masks", ymask)

    # Display original image with objects detected overlay
    cv.namedWindow("detected circles", cv.WINDOW_NORMAL)
    cv.imshow("detected circles", src)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])