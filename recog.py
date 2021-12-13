import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('Capture.jpg')
size = img.shape

width = int(size[1]) * 2
height = int(size[0]) * 2
img = cv2.resize(img, (width, height))

cv2.imshow("Result", img)
cv2.waitKey(0)
