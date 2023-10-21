import time
import random

print("--=================================================刚细出品======================================================--")
time.sleep(3)

print('ClearingScreen...')
time.sleep(2)

for i in range(30):
    print("♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂")
    time.sleep(0.2)

time.sleep(2)

a = input("Are you a stupid guy ? (o≖◡≖)  [yes]or[no]      ")  

def start():

    difficulty = input("Choose a difficulty !   o(≧口≦)o   [difficult] or [easy]  ")
    time.sleep(2)
    if (difficulty == "difficult"):
        guess = random.randint(0,50)
        
    elif (difficulty == "easy"):
        guess = random.randint(0,10)

    else:
        print("sorry,I can't understand  （～￣▽￣～）")
        time.sleep(3)
        print("So I think you may like a new difficulty [Fuker]   ( ˘•ω•˘ )ง  ")
        time.sleep(4)
        print("Let's do it !  （￣︶￣） ")
        time.sleep(2)
        guess = random.randint(50,150)
        
    for i in range(10) :
        number = int(input('What is it ?    '))
        if (number < guess):
            print("too small  （；´д｀）ゞ  ")
        if (number > guess):
            print("too big   (。_。)  ")
        if (number == guess):
            print ("yes that is right   (๑•̀ㅂ•́)و✧  ")
            time.sleep(1)
            print("What a stupid guy !   o(*≧▽≦)ツ ")
            time.sleep(2)
            end()

def end():
    a = input("Play angan?         ( *￣▽￣)")
    if a == ("yes"):
        start()
    else:
        quit()
        

if (a == 'yes'):
    print("OK ! ")
    time.sleep(1)
    print("Welcome to [STUPID GUESSING]")
    print("(￣▽￣)～■干杯□～(￣▽￣)")
    time.sleep(4.5)
    name = input('What is your name?     ')
    print('OK,' + name)
    time.sleep(2)
    print('What a stupid name ! Just fuking like you   ')
    print(" *´∀`)´∀`)*´∀`)*´∀`) ")
    time.sleep(4)
    print("Then,let us just guess a stupid number frist ")
    print("<(￣︶￣)↗[GO!]")
    time.sleep(5.5)
    start()
    
else:
    print("      ┑(￣Д ￣)┍      ")
    time.sleep(2)
    print("OK just fuck out there   (-_-) ")
    time.sleep(3.5)
    print("because you are so smart ! ")
    print("(。・_・)/~~~")
    time.sleep(4)
    quit()
