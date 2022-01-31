from src.date import dateFormatted
from src.logger import logger
import time
import mss
from cv2 import cv2
import numpy as np
from pyclick import HumanClicker
import pyautogui

hc = HumanClicker()

def clickbtn(img, name=None, timeout=3, threshold=0.7, deslogar=False):
    logger(None, progress_indicator=True)
    if name is not None:
        pass
        
    start = time.time()
    clicked = False
    while not clicked:
        matches = positions(img, threshold=threshold)
        print(len(matches))
        if len(matches) == 0:
            hast_timed_out = time.time() - start > timeout
            if hast_timed_out:
                if name is not None:
                    pass
                return False
            continue

        x, y, w, h = matches[0]
        pos_click_x = x + w / 2
        pos_click_y = y + h / 2
        movetowithrandomness(pos_click_x, pos_click_y, 1)
        pyautogui.click()
        
        if deslogar is True:
            movetowithrandomness(pos_click_x - 20, pos_click_y + 50, 1)
            pyautogui.click()
            time.sleep(10)
            movetowithrandomness(pos_click_x - 10, pos_click_y + 50, 1)
            pyautogui.click()

        return True
    
    
def positions(target, threshold=0.7, img=None):
    if img is None:
        img = printscreen()
    result = cv2.matchTemplate(img, target, cv2.TM_CCOEFF_NORMED)
    w = target.shape[1]
    h = target.shape[0]

    yloc, xloc = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    return rectangles

def printscreen():
    output_filename = 'screenshot.png'
    with mss.mss() as sct:
        sct.shot(output=output_filename)
        monitor = sct.monitors[0]
        sct_img = np.array(sct.grab(monitor))
        return sct_img[:, :, :3]
    
def movetowithrandomness(x, y, t):
    hc.move((int(x), int(y)), t)
