import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('Capture.JPG')
size = img.shape

width = int(size[1]) * 2
height = int(size[0]) * 2
img = cv2.resize(img, (width, height))

cv2.imshow("Result", img)
cv2.waitKey(0)

text = pytesseract.image_to_string(img)
print(text)
print(type(text))

temp = ""
for x in text:
    if x == "\n":
        temp += " "
    else:
        temp += x

print(temp)

#if "\n" in text:
    #print("There is a new line character in text")

arr = ["e", "d"]

print(type(arr))
