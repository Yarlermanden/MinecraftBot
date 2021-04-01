from mss import mss
from PIL import Image
import numpy as np
import time
import cv2

class ScreenReader():
    def __init__(self):
        self.width = 2560
        self.height = 1440

    def mss_record(self, width, height, startX, startY):
        with mss() as sct:
            monitor = {'top': startY, 'left': startX, 'width': width, 'height': height}
            img = sct.grab(monitor)
            return Image.frombytes('RGB', img.size, img.bgra, 'raw', 'RGBX')

    def capture_screen(self, showImage):
        frame = self.mss_record(self.width, self.height, self.width, 0)
        frame = np.array(frame)
        #frame = cv2.resize(frame, dsize=(160,90), interpolation=cv2.INTER_CUBIC)
        frame = cv2.resize(frame, dsize=(320,180), interpolation=cv2.INTER_CUBIC)
        if showImage:
            self.show_image('img', frame)

        return frame

    def show_image(self, name, image):
        cv2.imshow(name, image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
