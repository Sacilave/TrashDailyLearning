import time, pyautogui
time.sleep(3)
for i in range(3):
    time.sleep(2)
    a = pyautogui.position()
    print(a)
