import pyautogui
im = pyautogui.screenshot(region=(0,0, 300, 400))
im.save("screen.jpg")