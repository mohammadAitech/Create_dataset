import cv2 as cv
import os
import numpy as np

def create_dataset(pages):
    file_path = [f for f in os.listdir(f'pelak/{pages}') if f.endswith(('.jpg', '.png', '.jpeg'))]
    x_list = []
    y_list = []

    for filename in file_path:
        im = cv.imread(f"pelak/{pages}/" + filename)
        if im is None:
            print(f"Failed to load image: {filename}")
            continue
        im_resized = cv.resize(im, (8, 32))
        im_gray = cv.cvtColor(im_resized, cv.COLOR_BGR2GRAY)
        im_flatten = im_gray.flatten()
        x_list.append(im_flatten)
        y_list.append(pages)

    x = np.array(x_list)
    y = np.array(y_list)

    return x, y
