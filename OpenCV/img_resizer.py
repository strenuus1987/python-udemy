import cv2
import glob

f_list = glob.glob("*.jpg")

for f_name in f_list:
    img = cv2.imread(f_name, 1)
    img_resized = cv2.resize(img, (100, 100))
    cv2.imwrite("resized_" + f_name, img_resized)
