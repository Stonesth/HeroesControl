# importing the module
import time
import cv2
import pyautogui


# https://infoforall.fr/python/python-act260.html
# https://www.jeuxvideo.com/forums/42-47-40366992-1-0-1-0-python-tracking-d-objet-sur-ecran.htm
# https://www.google.com/search?q=pyautogui+locateCenterOnScreen+exemple&sxsrf=AOaemvIGXY8jmlSz1twi3OKFDtjFJFNOrQ%3A1634759401030&ei=6XJwYcqXAbGM9u8P7f2skAg&ved=0ahUKEwiKsJCr4dnzAhUxhv0HHe0-C4IQ4dUDCA4&uact=5&oq=pyautogui+locateCenterOnScreen+exemple&gs_lcp=Cgdnd3Mtd2l6EAMyBwghEAoQoAE6BwgAEEcQsAM6BAghEBVKBAhBGABQwfcDWK6DBGCphQRoAXACeACAAdUBiAHxB5IBBTAuNi4xmAEAoAEByAEIwAEB&sclient=gws-wiz
# https://pyautogui.readthedocs.io/en/latest/screenshot.html#the-screenshot-function
# https://www.programcreek.com/python/example/103347/pyautogui.locateOnScreen
# https://stackoverflow.com/questions/32156019/pyautogui-locatecenteronscreen-returns-none-instead-of-coordinates
# https://python.hotexamples.com/fr/site/file?hash=0xeda5c1b5d01397bf34028ff026acde669d0326ede8da316d2c6b8a1037b54761&fullName=python-master/sushigoroundbot.py&project=flow0787/python
# https://pypi.org/project/opencv-python/
# https://www.google.com/search?q=python+print-screen&oq=python+print-screen&aqs=chrome..69i57.14812j0j1&sourceid=chrome&ie=UTF-8
# https://datatofish.com/screenshot-python/

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' +
					str(y), (x,y), font,
					1, (255, 0, 0), 2)
		cv2.imshow('image', img)

	# checking for right mouse clicks	
	if event==cv2.EVENT_RBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) + ',' +
					str(g) + ',' + str(r),
					(x,y), font, 1,
					(255, 255, 0), 2)
		cv2.imshow('image', img)

# driver function
if __name__=="__main__":

	# reading the image
	# img = cv2.imread('/Users/thononpierre/Documents/Projet/Python/Project/HeroesControl/screenshot.png')
	img = cv2.imread('/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot.png')

	# displaying the image
	cv2.imshow('image', img)

	# setting mouse handler for the image
	# and calling the click_event() function
	cv2.setMouseCallback('image', click_event)

	# sleep for 1 second to wait for the image to be displayed
	time.sleep(1)
	
	# Move the mouse and click to the coordonate x and y
	pyautogui.click(2286 - (2286 / 2), 1709 - (1709 / 2) )

	# wait for a key to be pressed to exit
	cv2.waitKey(0)

	# close the window
	cv2.destroyAllWindows()

# # Take the printscreen of the full screen
# myScreenshot = pyautogui.screenshot()
# myScreenshot.save('screenshot.png')

# # reading the image
# img = cv2.imread('screenshot.png', 1)

# # displaying the image
# cv2.imshow('image', img)


