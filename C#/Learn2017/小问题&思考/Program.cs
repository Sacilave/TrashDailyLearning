using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 一些神奇的小问题和思考
{
    class Program
    {
        static void Main(string[] args)
        {
            // 在这里选择运行的类
            str1();
        }
        // 对数字叠加进行拼接如(0123456789这样的拼接)
        static void str1()
        {
            string str = "";
            for (int i = 0; i < 10; i++)
            {
                str += i.ToString();
            }
        }

        // 关于字符数组的存储在栈中还是堆中和引用的指向
        static void tip1()
        {
            string[] strArr = new string[] { "a", "b", "c" };
            // 因为 strArr 这个数组是引用类型，所以是在栈中存储引用的，在堆中的数据中是相对应的开辟内存块，在此便是 3 块， 但是因为 string 也是引用类型，所以这三块内存块存储的还是引用，是这三个字符串的引用
        }
    }
}
