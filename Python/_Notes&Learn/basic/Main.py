# 视频看到245:03
# 导入模块
import time  # 全部导入
from math import *  # 也是全部导入(从time模块中导入全部)
from time import daylight  # 从time模块中导入daylight
import math as mt  # 导入 math 模块 并作为 mt (以后便可以直接使用mt进行使用)

# 数据类型
def _type():
    string1 = "233"
    # 类型转换
    int(string1)
    str(string1)
    float(string1)
    bool(string1)
    # 获取元素类型
    print(type(string1))

# 字符操作
def _list():
    list1 = 'Hello world!'
    # 索引（从0开始计算）
    print(list1[0])    # 打印list1中的第1个字符
    print(list1[-1])   # 打印list1中倒数第1个字符
    print(list1[0:3])  # 打印list1中第1个到第3个字符
    print(list1[1:])   # 打印list1中从第2个字符开始往后的所有字符（包括第二个！）
    print(list1[:4])   # 打印list1中从第4个开始到第一个的字符

    # 占位符
    name = "ass"
    print(f"I am a {name}")  # 使用f"{变量}"格式可以使变量的值自动填充进{}中

    # 计算字符串长度
    print(len(list1))

    #对于字符的更多方法
    print(list1.upper())  #全改为大写
    print(list1.lower())  #全改为小写
    print(list1.find('H'))  #返回指定字符索引值（注意：这个有大小写敏感）
    print(list1.replace('Hello', 'Fuck'))  #替换字符
    print('Hello' in list1)  #判断指定字符是否在指定字符串（返回值为bool）
    print(list1.title())  #把每个单词的开头转为大写

# 运算符（懒得写了，跟C#差不多）
def _count():
    # 乘方
    print(3 ** 2)  # 3的2次方
    # 优先运算级
    print(2 * 3 ** 2)  #就跟数学一样呢

# 使用 类(class) 创建新类型
class Loli:  # 此时创建了一个 Loli 类
    def __init__(self, name, age):  # 这是一个构造函数，__init__()就是构造函数的语法
        self.name = name  # 此时的 self.name 中的 self 的作用就跟 C# 中的 this 作用一样
        self.age = age
    def setAge(self, age):
        self.age = age
    def setName(self, name):
        self.name = name
    def getAge(self):
        return self.age
    def getName(self):
        return self.name
    def sayHello(self):
        return f"hello, I'm {self.name}"
loli01 = Loli("Sylvie", 11)
loli01.setAge(12)
print(loli01.getAge(), loli01.getName())
print(loli01.sayHello())  # 妈的。。。寂寞的我写萝莉举例程序当成RPG了，越写越爽。。草(太寂寞了。。别生草了)

# 类的继承
# 现在定义一个需求：dog 类，cat 类，两个都有相同的 walk 功能。可以使用 继承 的方法来避免写两次相同的代码
class Mammal:  # 定义了一个类为 Mammal，其中有 walk 这个功能
    def walk(self):
        print("I'm fucking walking")
class Dog(Mammal):  # 在此的 Dog 类通过 class Dog(被继承的类) 这个语法继承了 Mammal 的功能
    pass  # 不写空语句会报错
class Cat(Mammal):
    pass
dog01 = Dog()
dog01.walk()  # it works !


