import time
import pyautogui
import os
from os.path import dirname
from PIL import Image
from keyboard import press_and_release




# trouver la position sur l'écran de l'image python
# https://www.google.com/search?q=trouver+la+position+sur+l%27%C3%A9cran+de+l%27image+python&sxsrf=AOaemvKKBKWJWMpr6q1Ebi323Ak5NTcfzw%3A1634737837696&ei=rR5wYbvtKYO-aJ-Bh-AI




# pos = pyautogui.locateCenterOnScreen('screenshot_1.png')
# print(pos)

# pyautogui.click(pos, duration=0.25)

# Take the printscreen of the full screen
# myScreenshot = pyautogui.screenshot()
# myScreenshot.save('screenshot.png')
   
# # Take the printscreen
# x1 = 1962
# y1 = 11
# x2 = 2002
# y2 = 45
# myScreenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
# myScreenshot.save('accessibility.png')





# pyautogui.click('screenshot_2.png', duration=0.25)

# press_and_release('cmd+tab')

# # Take the printscreen
# x1 = 1962
# y1 = 11
# x2 = 2002
# y2 = 45
# myScreenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
# myScreenshot.save('accessibility_8h36.png')
while True: # loop because it could be the blue or pink Play button displayed at the moment.
    pos = pyautogui.locateCenterOnScreen('accessibility.png')
    if pos is not None:
        break
    pos = pyautogui.locateCenterOnScreen('accessibility_8h36.png')
    if pos is not None:
        break
time.sleep(1)
print(pos)
print(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

pyautogui.click(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

   



# Controle de selection
while True: # loop because it could be the blue or pink Play button displayed at the moment.
    pos = pyautogui.locateCenterOnScreen('controle.png')
    if pos is not None:
        break
time.sleep(1)
print(pos)
print(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

pyautogui.click(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )



# Controle de selection
pyautogui.move(0,0)
while True: # loop because it could be the blue or pink Play button displayed at the moment.
    pos = pyautogui.locateCenterOnScreen('appareil.png')
    if pos is not None:
        break
time.sleep(1)
print(pos)
print(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

pyautogui.click(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )


# Controle de selection
pyautogui.move(0,0)
while True: # loop because it could be the blue or pink Play button displayed at the moment.
    pos = pyautogui.locateCenterOnScreen('iphone7.png')
    if pos is not None:
        break
time.sleep(1)
print(pos)
print(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

pyautogui.click(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

# # Take the printscreen
# time.sleep(3)
# x1 = 156
# y1 = 107
# x2 = 307
# y2 = 251
# myScreenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
# myScreenshot.save('connect.png')
# Controle de selection
pyautogui.move(1000,1000)
while True: # loop because it could be the blue or pink Play button displayed at the moment.
    pos = pyautogui.locateCenterOnScreen('connect.png')
    if pos is not None:
        break
time.sleep(1)
print(pos)
print(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

pyautogui.click(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

# # Take the printscreen
# x1 = 1970
# y1 = 904
# x2 = 2034
# y2 = 961
# myScreenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
# myScreenshot.save('controle_blue.png')
# Controle de selection
while True: # loop because it could be the blue or pink Play button displayed at the moment.
    pos = pyautogui.locateCenterOnScreen('controle_blue.png')
    if pos is not None:
        break
time.sleep(1)
print(pos)
print(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

pyautogui.click(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

# Take the printscreen
x1 = 1963
y1 = 8
x2 = 2014
y2 = 43
myScreenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
myScreenshot.save('accessibility_selected.png')
while True: # loop because it could be the blue or pink Play button displayed at the moment.
    pos = pyautogui.locateCenterOnScreen('accessibility_selected.png')
    if pos is not None:
        break
time.sleep(1)
print(pos)
print(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

pyautogui.click(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

# # try to find the image on the screen
# # various coordinates of objects in the game
# GAME_REGION = () # (left, top, width, height) values coordinates of the entire game window
# # calculate the region of the entire game
# GAME_REGION = (0, 0, 640, 400) # the game screen is always 640 x 480
# print('Game region found: %s' % (GAME_REGION,))


# def imPath(filename):
#     """A shortcut for joining the 'images/'' file path, since it is used so often. Returns the filename with 'images/' prepended."""
#     return os.path.join('', filename)

# # click on Play
# print('Looking for Play button...')


# while True: # loop because it could be the blue or pink Play button displayed at the moment.
#     pos = pyautogui.locateCenterOnScreen(imPath('terminal.png'), region=GAME_REGION)
#     if pos is not None:
#         break
# time.sleep(1)
# print(pos)

# pos = pyautogui.locateOnScreen('explorer.png')
# print(pos)


# pospoint = pyautogui.center(pos)
# print(pospoint)

# pyautogui.click(pospoint, duration=0.25)
# print('Clicked on Play button.')

# time.sleep(15)