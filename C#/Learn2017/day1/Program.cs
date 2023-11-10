// 引用命名空间(如：Console这个类便在System这个命名空间内)
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace day1  // 定义 命名空间(类的住址)
{
    class Program  // 定义 类(功能)
    {
        static void Main(string[] args)  // 程序从这里开始(主函数)
        {
            // 以下的 Title, WriteLine等均为方法，从Console这个类中调用的(用 . 来调用：类.方法)
            Console.Title = " This is title ";  // 设置标题
            Console.WriteLine("what's your fuking name : ");  // 输出自字符串(console是指控制台，也就是cmd)
            string name = Console.ReadLine();  // 定义变量name为读取(获取输入赋值到name变量中)
            Console.WriteLine("hello, " + name);  // 在窗口上输出(连接符为 + )
            Console.ReadLine();  // 对以上的文本进行访问(效果就是暂停窗口)

            //使用 #region 和 #endregion 把一段代码可折叠，如以下：
            #region
            Console.Write("dd");
            #endregion
        }
    }
}
