import pyautogui, time, random
'''
# 坐标草稿
Point(x=7, y=1080)  # win
Point(x=241, y=986)  # b站
Point(x=1111, y=322)  # v1
Point(x=1387, y=328)  # v2
Point(x=1719, y=320)  # v3
Point(x=1745, y=520)  # v4
Point(x=1394, y=509)  # v5
Point(x=1105, y=501)  # v6
Point(x=1157, y=665)  # 进入视频

# 获取坐标
time.sleep(3)
for i in range(1):
    time.sleep(3)
    a = pyautogui.position()
    print(a)
'''
''''''
# 设置变量
move_to = pyautogui.moveTo
click = pyautogui.click
a = duration=1

# 询问b站已经开启
i = input("智障，b站运行了么？[y/n]\n")

# 函数
def sjs():
    l = (random.choices([322, 509]))
    n = (random.choices([1111, 1387, 1719]))
    move_to(n[0], l[0], a)
    click()
    pyautogui.dragTo()

# 操作
if i == 'n':
    move_to(7, 1080, a)  # 按下win键
    click()
    move_to(241, 999, a)  # 打开b站
    click()
    time.sleep(3)
    sjs()
else:
    move_to(7, 1080, a)  # 按下win键
    click()
    move_to(241, 999, a)  # 打开b站
    click()
    time.sleep(1)
    move_to(5, 5, duration=1)
    pyautogui.doubleClick()
    sjs()



