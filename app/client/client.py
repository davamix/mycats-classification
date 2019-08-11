import requests
import cv2
import numpy as np
import struct

API_ENDPOINT = "http://localhost:5000/predict"

image_path = "./frame300a.jpg"

# Read image
img = cv2.imread(image_path)
img = cv2.resize(img, (299, 299))
img = np.reshape(img, [1, 299, 299, 3])
print(img.shape)

img_ser = img.tolist()

r = requests.post(API_ENDPOINT, json = {'data': img_ser})

print(r.text)