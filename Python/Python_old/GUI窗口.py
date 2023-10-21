import tkinter as tk  #导入GUI模块
import time

window = tk.Tk()  #定义
window.title('NumberGuessing')  #设置窗口标题
window.geometry('900x600')  #设置窗口大小200x100

l = tk.Label(window,text = ("Are you a stupid guy ? (o≖◡≖)  [yes]or[no]      "), bg='white', font=('Arial',12),width=70,height=17)  #text设置文本内容 bg背景颜色 font('字体',文字大小) 窗口大小(单位:文字数量)
l.pack()  #运行


window.mainloop()
