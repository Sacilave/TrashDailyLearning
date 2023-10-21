import time

import random
print("This is a realy stupid AI , you can ask me anything , suck as Free Talk ")
time.sleep(3)
a = input("Enter [yes] or [no] to me       ")

time.sleep(1)


def start():
        
    print("Welcome")
    time.sleep(1)
    print(random.choice(WQ))
    
    
    
    
    
WQ = ["How are you ?   ","Have you already ate yet ?   ","Have you already shit ?    ","How was your life these days ?    "]
    
    
    
if 'yes' in a:
    print('OK')
        
    start()
elif "no" in a:
        
    print("OK,fine,I don't care ")
        
    time.sleep(2)
    print("Just Fuck out there Bad Kid !")
    time.sleep(2)
    print("LogingOut......")
    time.sleep(1)
        
    for i in range(5):
            print("♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂你离开了刚细♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂♂")
    time.sleep(2)
    quit()


def get_time():   
    print (time.strftime(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))) # 打印当前年 月 日 时 分 秒
