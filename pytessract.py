import cv2
import os
import pytesseract
import time
from optimizer import ImageCompressor

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

PATH_TO_IMAGE = "test.webp"
NEW_PATH = ImageCompressor(PATH_TO_IMAGE)

text = pytesseract.image_to_string(NEW_PATH, lang='spa')

print("Texto reconocido:")
print(text)
print("Tiempo de proceso: ", time.process_time())

img_display = cv2.imread(NEW_PATH)

cv2.imshow('Imagen Optimizada', img_display)
cv2.waitKey(0)
cv2.destroyAllWindows()