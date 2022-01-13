import cv2
import pytesseract
import pyautogui


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('Capture.JPG')
size = img.shape

def resize(inIMG, inMultiplier):
    width = int(size[1]) * inMultiplier
    height = int(size[0]) * inMultiplier
    outIMG = cv2.resize(inIMG, (width, height))
    return outIMG

def configureText(inText):
    count = 0
    temp = ""
    for x in text:
        if x == "\n":
            if count == 0:
                temp += ""
                count += 1
            else:
                temp += " "
                count = 0
        elif x == "-":
            count = 0
            temp += x
        else:
            temp += x
    return temp

for i in range(3):
    img = resize(img, (i+1))

    cv2.imshow("Result", img)
    cv2.waitKey(0)

    text = pytesseract.image_to_string(img)
    print(configureText(text))
#print(text)
#print(type(text))
#print(temp)

im1 = pyautogui.screenshot(region=(699, 438, 809, 463))
im1.save("")
