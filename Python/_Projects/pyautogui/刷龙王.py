import pyautogui, time, random
time.sleep(3)
def u():
    pyautogui.typewrite(y)
    pyautogui.press('space')
    pyautogui.hotkey('ctrl', 'enter')
while True:
    b = random.randint(2,10)
    c = random.randint(2,10)
    d = random.randint(2,10)
    for i in range(b):
        y = 'shuapingzhong'
        u()
    for s in range(c):
        y = 'zhekeshizhidonghuashuapingne'
        u()
    for h in range(d):
        y = 'gewaizhizhangne'
        u()

