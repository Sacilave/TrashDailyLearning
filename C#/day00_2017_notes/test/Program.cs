using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace test
{
    class Program
    {
        private static void Main()
        {
            int a = 1;
            // 装箱操作(比较消耗性能)：值类型 隐式转换 为 object 类型 或 由此值类型实现的任何接口类型的过程
            // 该过程为先在堆中开辟三块内存块，分别为 相同类型，同步块索引，类型对象指针的内存块。然后再把其中的 相同类型 的内存块的引用传递给object类型的 b
            object b = a;
            // 拆箱操作(比较消耗性能)：从object类型到值类型或从接口类型到实现该接口的值类型的显式转换
            // 该过程为先比较之前堆中开辟的数据类型是否与赋值对象数据类型相同，如果相同便把堆中的数据复制一份到 c 中
            int c = (int)b;

            // 经典实例：传参时要求为object类型，传递的参数为值类型(比如int)，就会造成拆装箱
            // 提示：尽量避免这种情况，可以使用 重载、泛型 避免，不过对于现在的硬件来说问题也不大，几百次的拆装箱没什么问题
        }

    }
}
