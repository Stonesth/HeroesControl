import time
import cv2
import pyautogui
from keyboard import press_and_release, press, release


# Take the printscreen at the coordonate x and y
myScreenshot = pyautogui.screenshot(region=(100, 100, 100, 100))
myScreenshot.save('screenshot_test3.png')
# reading the image
img = cv2.imread('screenshot_test3.png', 1)
# displaying the image
cv2.imshow('image', img)

# sleep for 1 second to wait for the image to be displayed
time.sleep(1)

# Move the mouse and click to the coordonate x and y
pyautogui.click(2286 - (2286 / 2), 1709 - (1709 / 2) )

# wait for a key to be pressed to exit
cv2.waitKey(0)
# close the window
cv2.destroyAllWindows()



