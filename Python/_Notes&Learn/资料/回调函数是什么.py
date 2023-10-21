# 回调函数(一个函数的参数列表中调用了另外一个函数)

# 首先定义函数 addHead(content) 用于在参数 content 前加 "前缀"
def addHead(content):
    content = "前缀"+content
    return content

# 再定义一个函数 add(content, function) 用于返回："前缀" + content + "后缀"
def add(content, function):
    # 这里使用参数列表中的 function 参数，并作为一个函数传递了参数列表中的另一个参数 content
    return function(content)  # 返回结果为 function(content) 的返回值

# 这里是主运行
def main():
    # 调用 add() , 并传参: "123" 和 addHead
    print(add("123", addHead) + "后缀")  # 此时的传递的 addHead 就是第一个定义的函数(相当于把第一个函数传递给 add() 中的 function函数)


if __name__ == "__main__":
    main()


""" 举例一个故事（转自：https://www.zhihu.com/question/19801131 作者：常溪玲）
你到一个商店买东西，刚好你要的东西没有货，于是你在店员那里留下了你的电话，过了几天店里有货了，
店员就打了你的电话，然后你接到电话后就到店里去取了货。在这个例子里，你的电话号码就叫回调函数，
你把电话留给店员就叫登记回调函数，店里后来有货了叫做触发了回调关联的事件，店员给你打电话叫做
调用回调函数，你到店里去取货叫做响应回调事件。回答完毕。
"""