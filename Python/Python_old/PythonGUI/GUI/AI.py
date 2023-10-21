import time
import random
print("This is a realy stupid AI , you can ask me anything , suck as Free Talk ")
# time.sleep(3)
began = input("Enter [yes] or [no] to me       ")


# 定义
good_feel = ['fine', 'good' , 'well' , 'perfect']
bad_feel = ['bad', 'worse', 'poor']
yes_answer = ['yes', 'sure' , 'of course','certainly','yup','ok']
no_answer = ['no', 'not',"isn't","aren't","doesn't","wasn't"]
call_me = ['me','i']
call_other = ['he','she','it','that','this']
call_others = ['them','these','those']

def anwei():
    anwei_tell = ["All things will be fine ","Never mind ! ","Don't worry,that's not important. ","Cry may help you to feel better ","Just Forget it ! ","Why you so care for this thing ! "]
    print(anwei_tell)
    time.sleep(4)
    anwei_i = input("Don't be so said,talk to me, ok?")
    if yes_answer in anwei_i:
        print("That's ok , Hope things work out")
    else:
        print("Oh ! Fine ! I don't care ! ")
def start():
    print("Welcome")
    time.sleep(1)
    start_ask = random.choice(WQ)
    i_s_q = input('How are you')

    if "How are you ?"or"How was your life these days ?" in start_ask:
        if i_s_q in call_me:
            if i_s_q in good_feel:
                if i_s_q in no_answer:
                    anwei()
                else:
                    print("That's enough.You good,I good")
            if i_s_q in bad_feel:
                print("really ?")
                time.sleep(1)
                anwei()


WQ = ["How are you ?   ","Have you already ate yet ?   ","Have you already shit ?    ","How was your life these days ?    "]



if 'yes' in began:
    print('OK')
    start()
elif "no" in began:
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
