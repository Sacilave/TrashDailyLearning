#pylint:disable=E0001
import time
import random

# --------- VARIABLES ---------

money = 0
difficulty = 0
friend = 0
life = 4
power = 100
hunger = 0
food = 10
medicine = 0
friend_money_c = 0
friend_power_c = 0

# ----------FUNCTIONS----------

def decide():
    global hunger
    hunger = hunger + 1
    if 0 < life <= 1:
        print("You need treatment !")
        time.sleep(2)
    if life <= 0:
        time.sleep(1)
        print("\nYour life: ", life)
        print("———— GAME OVER ————")
        time.sleep(3)
        quit()
    if hunger >= 250:
        time.sleep(1)
        print("\nYour hunger: ", hunger)
        print("———— GAME OVER ————")
        time.sleep(3)
        quit()

def make_friend():
    global friend, friend_money_c, friend_power_c
    c = input(
        "\nwho you want fight with him : Enter[fight with]\nwho you want play with him : Enter[play with]\nwho you want work with : Enter [work with]\n")
    age = random.randint(16, 100)
    friend_power = random.randint(10, 1000)
    IQ = random.randint(0, 300)
    friendliness = random.randint(10, 50)
    reach_thing = random.randint(2, 15)
    money_make = random.randint(0, 100)
    a = random.choice(["Steve", "Jack", "Tim", "Ezio", "Anno", "Tony", "Jone", "John", "Mike", "Tom"])
    b = random.choice(["Simon", "vincent", "richie", "gilbert", "rick", "james", "luther", "regan", "daniel", "Stark"])
    friend_name = (a, b)
    time.sleep(1)
    print()

    # --- Fight with ---

    if "fight" in c:
        print("His name: ")
        print(a, b)
        print("His age: ", age)
        print("His power", friend_power)
        print("He can do: ", reach_thing, " thins")
        time.sleep(4)

        b = input("Make friend with him?\n[Yes] or [No] :\n ")
        global friend
        if "yes" in b:
            friend = friend + 1
            print("Your friends:", friend)
            friend_power_c = friend_power_c + friend_power
            print("Your friends can help you to make ", friend_money_c, " $")
            time.sleep(3)
            menu()
        else:
            d = input("OK,Try again?")
            if "yes" in d:
                make_friend()
            else:
                print("See you !")
                time.sleep(2)
                menu()

    # --- Play with ---

    if "play" in c:
        print("His name:")
        print(a, b)
        print("His age: ", age)
        print("His friendliness: ", friendliness)
        print("His IQ: ", IQ)
        if IQ < 88:
            print("You can have a fun time with this stupid!")
        time.sleep(4)

        b = input("Make friend with him?\n[Yes] or [No] :\n ")

        if "yes" in b:
            friend = friend + 1
            print("Your friends:", friend)
            time.sleep(2)
            menu()
        else:
            d = input("OK,Try again?")
            if "yes" in d:
                make_friend()
            else:
                print("See you !")
                time.sleep(2)
                menu()

    # --- Work with ---

    if "work" in c:
        print("His name: ")
        print(a, b)
        print("His age: ", age)
        print("He can do ", reach_thing, " things")
        print("Money he can make: ", money_make, " $")
        time.sleep(4)

        b = input("Make friend with him?\n[Yes] or [No] :\n ")

        if "yes" in b:
            friend = friend + 1
            print("Your friends:", friend)
            friend_money_c = friend_money_c + money_make
            print("Your friends can help you to make ", friend_money_c, " $")
            time.sleep(3)
            menu()
        else:
            d = input("OK,Try again?")
            if "yes" in d:
                make_friend()
            else:
                print("See you !")
                time.sleep(2)
                menu()

def rename():
    global name
    name = input("Ezio: What's your name ? \nIf you don't have a name\nenter[rename],I will give you a name!\n")
    if "rename" in name:
        random_name()
        name = c
    else:
        print("Your name: ", name)
        time.sleep(3)

def get_time():
    print(time.strftime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    time.sleep(3)

def write_stories():
    a = input("The story's name\n")
    t = time.strftime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print(a, ":", )
    print(t)
    story_input = input("  ")
    story = open('story.txt', 'a', encoding="utf-8")
    story.write("\n")
    story.write(a)
    story.write('\n')
    story.write(t)
    story.write("\n")
    story.write(story_input)
    story.close()
    time.sleep(2)

def fight():
    global power, life, friend_power_c
    print()
    print("Finding players ...")
    time.sleep(random.randint(0, 5))
    difficulty = random.randint(0, 9999)
    print("Difficulty: ", difficulty)
    time.sleep(2)
    print("Your power: ", power)
    print("Your friends' power: ", friend_power_c)
    print("The whole power from you : ", power + friend_power_c)
    time.sleep(3.5)
    a = input("Fight with him? \n")
    if "yes" in a:
        print("Fighting...")
        time.sleep(1)
        if power + friend_power_c <= difficulty:
            may = random.randint(0, 10)
            if may < 9:
                print("You lost!")
                life = life - 2
                time.sleep(1)
                print("Your life: ", life)
            if may > 9:
                print("You win!")
                power = power + 20
                time.sleep(1)
                print("Your power: ", power)
            if may == 9:
                print("Neither of you are win or lost")
                time.sleep(2)
        else:
            print("You win !")
            power = power + 5
            time.sleep(1)
            print("Your power: ", power)
    else:
        print("Well,we can find others!")
        time.sleep(2)
        fight()
    time.sleep(2)

def challenge():
    global life, power
    time.sleep(2)
    a = input("\nAre you sure you want to do this?\nIf you join this fight ,you can not out unless you win!\n")
    if "no" in a:
        menu()
    print("Ok, never give up!")
    time.sleep(2)
    difficulty=random.randint(29999,50000)
    g = random.randint(100,20000)
    p = random.randint(99, 9999)
    print("His power: ", difficulty)
    print("Your power: ", power)
    d = input("Keep fighting?\n")
    if "no" in d:
        print("Ok, See you .")
        time.sleep(2)
        menu()
    if power + friend_power_c + g < difficulty:
        print("You Lost .")
        life = life - 5
        print("Your life: ", life)
        time.sleep(3)
        menu()
    else:
        print("You win !!!")
        time.sleep(1)
        print("But how can you do this! ")
        time.sleep(2)
        print("You will get a big gift . ")
        time.sleep(2)
        power = power + p
        print("Your power: ", power)
        time.sleep(2)
        print("It's a surprise,right?'")
        time.sleep(2)
        print("Challenge more to get more power! See you .")
        time.sleep(3)
        menu()

def random_name():
    a = random.choice(["Steve", "Jack", "Tim", "Ezio", "Anno", "Tony", "Jone", "John", "Mike", "Tom"])
    b = random.choice(["Simon", "vincent", "richie", "gilbert", "rick", "james", "luther", "regan", "daniel", "Stark"])
    global c
    c = (a, b)
    print("Your name: ")
    print(a, b)
    time.sleep(3)

def eat():
    global hunger, food
    print("Your hunger: ", hunger, "\nYour food: ", food)
    time.sleep(2)
    s = int(input("How many food do you want to spend ?\n"))
    if s < 0:
        print("I know that you are just kidding.")
        time.sleep(2)
        menu()
    elif food < s:
        print("Your food is not enough!")
        time.sleep(2)
        print("Please buy more food to eat.")
        time.sleep(2)
        menu()
    else:
        c = s * 5
        hunger = hunger - c
        food = food - s
        print("Your food: ", food)
        print("Your hunger: ", hunger)
        time.sleep(3)
        menu()

def treatment():
    global medicine, life
    a = int(input("How much medicine do you want to use?\n--[Use one medicine to restore one life]--\n"))
    if a < 0:
        print("Are you want to die ?")
        time.sleep(1)
        print("Fuck out there !!")
        time.sleep(2)
        menu()
    elif medicine < a:
        print("Your medicine is not enough !")
        time.sleep(2)
        menu()
    else:
        medicine = medicine - a
        life = life + a
        print("Your medicine: ", medicine)
        print("Your life: ", life)
        time.sleep(3)
        menu()

def make_money():
    global money
    time.sleep(1)
    a = input("Who will go to make money ?\n[I] or [My Friends]?\n")
    if 'I' in a:
        print("\n-——————————- Working -——————————-\n")
        time.sleep(2)
        print("2000 Years Later ···")
        time.sleep(2)
        g = power / 10
        money = money + g
        print("Your money: ", money, " $")
        time.sleep(2)
        menu()
    if 'friend' in a:
        if friend <= 0:
            print("Are you kidding ?  You have no friend !")
            time.sleep(3)
            menu()
        else:
            print("\n—— Friends are working ——\n")
            time.sleep(1)
            money = money + friend_money_c
            print("Your money:  ", money, " $")
            time.sleep(3)
            menu()

def buy():
    global money, medicine, food

    print("———————————————————— GX Shop ————————————————————")
    time.sleep(1)
    print("Commodity:")
    print("[Medicine]      [Food]")
    e = input("Your decision: \n")
    if "medicine" in e:
        a = int(input("How much medicine do you want to buy ?\n--($40 each)--\n"))
        if a < 0:
            print("······\nJust go to hill.")
            time.sleep(2)
            menu()
        elif money < a * 40:
            print("Your money is not enough !\nWork hard to make money !")
            time.sleep(3)
            menu()
        else:
            b = a * 40
            money = money - b
            medicine = medicine + a
            print("Your money: ", money, " $")
            print("Your medicine: ", medicine)
            time.sleep(3)
            menu()
    if "food" in e:
        r = int(input("How much food do you want to buy ?\n--($20 each)--\n"))
        if r < 0:
            print("You are kidding !")
            time.sleep(2)
            menu()
        elif money < r * 20:
            print("Your money is not enough !\nWork hard to make money !")
            time.sleep(3)
            menu()
        else:
            v = r * 20
            money = money - v
            food = food + r
            print("Your money: ", money, " $")
            print("Your food: ", food)
            time.sleep(3)
            menu()

def self_information():
    global money, friend, life, power, hunger, food, medicine, friend_money_c, friend_power_c, name
    print("\nYour information:\n")
    print("Name: ", name)
    print("Money: ", money, " $")
    print("Friends: ", friend)
    print("Life: ", life)
    print("Power: ", power)
    print("Hunger: ", hunger)
    print("Food", food)
    print("Medicine", medicine)
    print("Your friends can help you to make ", friend_money_c, " $")
    print("Your friends' power: ", friend_power_c)
    time.sleep(8)

def play_guide():
    print()
    print("1.Do not enter any capital letter!\n2.Enter the same word as the words on menu (This is not an AI ...)")
    print("3.The best to enter 'yes' or 'no' to answer.\nLast: REMEMBER ! This boring game made by GX·GAME ！")

# ----------MAIN----------

def training():
    global power, life
    print()
    print("Finding players ...")
    time.sleep(random.randint(0, 5))
    difficulty = random.randint(1, 500)
    print("Difficulty: ", difficulty)
    time.sleep(2)
    print("Your power: ", power)
    time.sleep(2)
    a = input("Fight with him? \n")
    if "yes" in a:
        print("Fighting...")
        time.sleep(1)
        if power <= difficulty:
            f_may = random.randint(0, 10)
            if f_may <= 5:
                print("You lost!")
                life = life - 1
                time.sleep(1)
                print("Your life: ", life)
            if f_may >= 6:
                print("You win!")
                power = power + 5
                time.sleep(1)
                print("Your power: ", power)
        else:
            print("You win !")
            power = power + 5
            time.sleep(1)
            print("Your power: ", power)
    else:
        print("Well,we can find others!")
        time.sleep(2)
        training()
    time.sleep(1)
    print("\nEzio:So now you know how to be stronger.\n")
    time.sleep(2)
    print("let's start!")
    time.sleep(1)
    main()

def start():
    print("\nEzio: Hello,I am Ezio !")
    time.sleep(1)
    print("Ezio: You are ", name, "right?")
    time.sleep(2)
    print("Ezio: OK !")
    time.sleep(1)
    a = input("Are you ready to start this exciting journey ? \n")
    if "yes" in a:
        print("\nEzio: That's good ! \n")
        time.sleep(1)
        print("Ezio: So let's have a training first.")
        time.sleep(2)
        training()
    else:
        print("Ezio: Fine.")
        time.sleep(1)
        print("You can leave here.")
        time.sleep(2)
        quit()

def main():
    menu()

def menu():
    print()
    decide()
    print()
    time.sleep(1)
    print("Menu:\n[Fight]             [Write Stories]\n[Make Friends]      [Eat]\n[Buy]               [Treatment]\n[Work]              [Time]\n[Rename]            [Personal information]\n[Challenge]         [Visit Guide]")
    a = input("Choose a action\n")
    if "fight" in a:
        fight()
        menu()
    elif "write stor" in a:
        write_stories()
        menu()
    elif "make friend" in a:
        make_friend()
    elif a == "eat":
        eat()
    elif "treatment" in a:
        treatment()
    elif "buy" in a:
        buy()
    elif "work" in a:
        make_money()
    elif "time" in a:
        get_time()
        menu()
    elif "rename" in a:
        rename()
        menu()
    elif "personal information" in a:
        self_information()
        menu()
    elif "challenge" in a:
        challenge()
    elif "visit guide" in a:
        play_guide()
        menu()
    else:
        print("I guess you have just enter the wrong message.")
        time.sleep(3)
        print("Enter the right words to use these functions")
        time.sleep(1)
        menu()

# ----------START----------

print()
time.sleep(1)
print(")-—————-|||-———-[   HEART OF BORING   ]-———-|||-—————-(")
print()
print("                                       —————— GX·GAME")
time.sleep(2)
i_start = input("Etner [Start] to login ... \nEnter [Quit] to quit ... \nEnter [Visit Guide] to know how to play this game\n")
if "no" in i_start:
    quit()

elif "start" in i_start:
    print("---————————————————login————————————————--- \n")
    time.sleep(1)
    rename()
    start()
else:
    print("It seems that you don't know how to play.")
    time.sleep(2)
    print("I will tell you some attentions.")
    time.sleep(2)
    play_guide()
    l = input("So just one question: do you want to play this game? \n")
    if "yes" in l:
        rename()
        start()
    else:
        print("OK,just fuck out there ")
        time.sleep(2)
        quit()

#  Made  by   GX - GAME
