import cv2
import os

def verify_image_color(path):
    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    diff_img = cv2.absdiff(img, img_gray)
    sum_diff = diff_img.sum()
    if sum_diff == 0:
        return False
    if sum_diff != 0:
        return True