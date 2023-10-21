import pyautogui, time, random

move = pyautogui.moveTo
click = pyautogui.click
a = duration=2
move(7, 1080, a)  # 按下win键
click()
move(574, 601, a)
click()
b = random.choices([229, 366, 517])
move(1391, b[0], a)
click()
