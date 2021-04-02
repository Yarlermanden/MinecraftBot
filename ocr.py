from PIL import Image
import pytesseract
import cv2
import numpy as np
from matplotlib import cm

import time
class OCR:
    def __init__(self):
        #self.tesseract = cv2.text.OCRTesseract_create()
        return

    def read_from_image(self, image):
        image = self.prepare_image(image)
        #text = pytesseract.image_to_string(image, config='outputbase digits')
        #text = pytesseract.image_to_string(image, config=r'--oem 3 --psm 10 digits')
        #text = tesseract.run(img, 0)
        #print('ocr: ' + text)
        x = 0
        for i in image:
            for j in i:
                if j == 255:
                    x = x+1
        return x

    def prepare_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        (x, image)  = cv2.threshold(image, 254, 255, cv2.THRESH_BINARY)
        cv2.imshow('s', image)
        return image
