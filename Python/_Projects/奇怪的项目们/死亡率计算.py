import random
import time

print()
print("——————死亡率计算——————")
print("-- Massage Source: \n   https://wenku.baidu.com/view/17b437f7cfc789eb162dc897.html")
print()

s = "你的死亡率: \n"
c = ["出门坐在大街上", "从10层楼跳下", "全身浸泡在水中5个小时", "去和群狼打架", "去吃点有毒的", "跳入火山", "到大街上砍人", "当着网吧里所有人的面拔掉网线", "刺杀习近平(推荐是特朗普哦,亲)", "用各种刀具在心脏或是要害处用力捅几刀", "飙车狂撞其他车(当成自己处于GTA)", "持续玩电脑24小时以上"]

a = int(input("Your age: \n"))
if a < 0:
    print("正经点")
if 0 <= a < 5:
    print(s,"0.045%")
if 5 <= a < 10:
    print(s,"0.028%")
if 10 <= a < 15:
    print(s, "0.029%")
if 15 <= a < 20:
    print(s,"0.041%")
if 20 <= a < 25:
    print(s, "0.053%")
if 25 <= a < 30:
    print(s, "0.061%")
if 30 <= a < 35:
    print(s, "0.082%")
if 35 <= a < 40:
    print(s, "0.120%")
if 40 <= a < 45:
    print(s, "0.188%")
if 45 <= a < 50:
    print(s, "0.311%")
if 50 <= a < 55:
    print(s, "0.441%")
if 55 <= a < 60:
    print(s, "0.680%")
if 60 <= a < 65:
    print(s, "1.112%")
if 65 <= a < 70:
    print(s, "1.864%")
if 70 <= a < 75:
    print(s, "3.359%")
if 75 <= a < 80:
    print(s, "5.620%")
if 80 <= a < 85:
    print(s, "9.351%")
if 85 <= a < 90:
    print(s, "14.417%")
if 90 <= a < 95:
    print(s, "20.734%")
if 95 <= a < 100:
    print(s, "19.812%")
if 100 <= a <= 120:
    print(s, "45.434%")
if a > 120:
    print("你怎么还没死！")
    b = input("需要提供死亡方法吗？")
    if "yes"or"是" in b:
        print(random.choice(c))
        time.sleep(2)
        print("You can try !\nJust do it !!!")
        time.sleep(2)
    else:
        print("OK,bye~")
        time.sleep(1)
        print("Don't forget to kill  [Donald John Trump]")
        time.sleep(2)
        quit()
