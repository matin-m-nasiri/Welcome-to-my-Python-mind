import cv2
import numpy as np
import pyautogui
import time

SC = (1920, 1080)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.2, (SC))

fps = 30
prev = 0
while True:
    time_elapsed = time.time() -prev

    img = pyautogui.screenshot()

    if time_elapsed > 1.0/fps:
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cytColor(frame, cv2.COLOR_RGB2YCrCb)
        out.write(frame)
    cv2.waitKey(100)

cv2.destroyAllWindows()
out.release()