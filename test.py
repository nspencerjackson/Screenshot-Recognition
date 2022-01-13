import pyautogui as pag

im1 = pag.screenshot("my_screenshot2.png", region=(699, 438, 100, 100))
im2 = im1.size
print(im2)
#im1.save("")
