// 引用命名空间(如：Console这个类便在System这个命名空间内)
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Move;

namespace day2  // 定义 命名空间(类的住址)
{
    // enums
    #region
    [Flags]  // 并无实际作用，用来标记该枚举可以调用多个
    enum PersonStyle
    {
        stupid = 1,   // 0000000001
        ass = 2,      // 0000000010
        shitty = 4,   // 0000000100
        fucking = 8,  // 0000001000
        cocky = 16    // 0000010000
    }
    /*
     选择多个枚举值
     * 运算符: | (按位或) --- 两个对应的二进制位中有一个为 1 , 结果为 1
     * 举例1：stupid | ass  -->  0000000001 | 0000000010  -->  0000000011
     * 举例2：ass | cocky   -->  0000000010 | 0000010000  -->  0000010010
     * 
     * 条件：
     * 1.任意多个枚举值做 | 运算 的结果不能与其他枚举值相同(所以值必须以2的n次方标识，如1, 2, 4, 6, 8等)
     *   解释简单一点就是比如 0000000001 | 0000000011 结果是 0000000011, 与前方第二者相同了，相当于是 1 和 3 输出了 3
     * 2.定义枚举时，应使用 [Flags] 特性修饰
     * 
     判断标志枚举是否包含指定枚举值
     * 运算符: & (按位与) --- 两个对应的二进制位都为 1 ，结果为 1
     * 举例1：0000000011 & 0000000001  -->  0000000001
     * 举例2：0000001001 & 0000001101  -->  0000001001
     */
    #endregion

    class Program  // 定义 类(功能)
    {
        // 关于新建方法本身
        #region
        // private: 对该方法进行封装，相对的可以换成 public 来使该方法公开
        // void: 方法的类型，当前方法为无类型，相对可以用其他的比如int, float, string等，但是需要返回值
        // string[] args: 在命令窗口输入的参数，简称: 命令行参数(在运行时会弹出命令窗口，可以在那里输入一些参数)
        //          args: 用来处理命令行参数
        private static void Main0(string[] args)
        {
            
        }
        #endregion

        // 各种小知识点
        #region
        
        // 拆装箱
        private static void Knowledge1()
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

        #endregion

        // 访问修饰符(访问级别)
        #region
        private void Private()
        {
            // 当前的访问修饰符是 private ，表示当前访问级别是只限制于当前的 类 中可以访问
        }
        public void Public()
        {
            // 当前的访问修饰符是 public ，表示当前访问级别是可以在其他各种类中使用
        }
        // 除了对于方法可以使用访问修饰符，对变量也可以使用（对于变量，一般使用 private 修饰符，如果想要在其他类中访问，可以创建一个修饰符为 public 的方法，通过方法进行访问）
        private int testInt0 = 0;
        #endregion

        // 占位符
        static void Main1(string[] args)
        {
            string name = "AK47";
            string number = "33";
            // 以下{0}，{1}均为占位符，与后面变量相对应，但是要使用string类中的Format方法
            Console.WriteLine(string.Format("name: {0} , number: {1} ", name, number));
            // 标准数字字符串格式化：以下占位符{0}对应后面的10，占位符中的 :c 表示一种格式：货币的格式
            Console.WriteLine(string.Format("金额: {0:c}", 10));
            // :d 表示在数字前增加位数，如以下的 5 是一位数，通过 d2 来把数字变成两位数，不足两位加0，满足两位不不改动（以此类推d3为改成三位数）
            Console.WriteLine(string.Format("金额: {0:d2}", 5));
            // :f 以指定精度来显示，如以下f1指以以为小数显示进行四舍五入，以下便输出结果3.3(以此类推f2便是以两位小数为基准来四舍五入)
            Console.WriteLine(string.Format("金额: {0:f1}", 3.26));
            // :p 以百分数输出，如以下：p0 输出10% ，p1输出10.0% ，p2输出10% ，p默认输出10.00%（自己看吧）
            Console.WriteLine(string.Format("百分比: {0:p}", 0.1));

            // 转义符：把指定字符转换成原始含义，如你他妈的想在""中再加一个"，就得用 \ 符，\" 便可使 " 表示原始含义
            Console.WriteLine(" \" ");
            // 神奇的就来了，论如何写一个空字符：\0 便是空字符了呢，' ' 像这种里面加个空格是完全不算的！不过空字符串倒是可以直接 "" 的
            Console.WriteLine('\0');
            // 其他的：\r\n 表示换行    \t 相当于按下了Tab键，空四格

            //多类型的加减乘除
            byte c = 1;
            short c1 = 2;
            int c2 = c + c1;   //这里的byte和short都是很小的数据类型，所以在相加的时候会自动提升为比他们高的类型，这里的便是int
            byte c3 = (byte)(c + c1);   //想要数据还是byte类型，要进行显式转换

            Console.ReadLine();
        }
        
        // 运算符
        static void Main2()
        {
            // 加 +      减 -      乘 *      除 /      取余数 %
            int num = 14 % 10;
            Console.WriteLine(num);
            Console.ReadLine();

            // 逻辑运算符：与(并且)：&& (一真俱真)     或(或者)：|| (一假俱假)    非：在值的前面加 ! (可以取反)
            // 短路逻辑：对于 && 和 || 会按照顺序来判断，比如对于 && 第一个值如果已经是false了，便不会计算剩下的了；|| 中第一个值如果已经是true了，便不会继续计算
            // 一般把计算量大的放前面
            bool num1;   // 只要出现一个false，便输出false
            num1 = true && true;   // 返回值：true
            num1 = true && false;   // 返回值：false
            num1 = false && true;   // 返回值：false
            num1 = false && false;   // 返回值：false
            bool num2;   // 只要出现一个true，便输出true
            num1 = true || true;   // 返回值：true
            num1 = true || false;   // 返回值：true
            num1 = false || true;   // 返回值：true
            num1 = false || false;   // 返回值：false
            bool num3;
            num3 = !true;   //返回值为false

            // 快捷运算符：+=     -=      *=      /=      (快捷运算符不会做类型提升)，比如byte += 2中byte不会升级类型为int
            int num4 = 1;
            num4 += 2;   //返回值：3，说明num4加了2加了再重新赋值给num4，即为 3，以此类推

            // 一元运算符(运算符的左或右只有一个值) 注意：只再下一行指令才开始有效！ ：++ 和 -- (备注：这他妈的是两个减号)
            // 解释：如以上的 true && false 中的&&运算符左右分别有true 和 false两个元，所以叫做二元运算符
            int num5 = 1;
            num5++;   //表示先返回值，再把num5这个变量自增1
            Console.WriteLine(num5);   //返回值：2  原因：不管是先加还是后加，他都自增了一次，在下一行指令输出的时候便是2了

            int num6 = 1;
            ++num6;   //表示先把num5这个变量自增1，再返回值
            Console.WriteLine(num6);   //返回值：2  原因同上

            int num7 = 1;
            Console.WriteLine(++num7);   //返回值：2  原因：先自增了一次(也就是先加了一次 1 )，再输出

            int num8 = 1;
            Console.WriteLine(num8++);   //返回值：1  原因：先输出，再自增，所以返回值还是原来的 1 呢

            // 三元运算符  结构： 数据类型 变量名 = 条件 ? (满足条件的)结果 : (不满足条件的)结果
            // 备注：结果是什么数据类型，开头的就写什么数据类型！！！
            string r1 = 6 < 7 ? "yes" : "no";

            // 优先级
            // 不多哔哔，就跟小学数学学的一样：先乘除后加减···括号里的先运算，但是，如果要用多个括号，请全用小括号
            int num9 = ((1 + 2) * 3) / 1;

        }

        // 各数据类型和其转换
        static void Main3()
        {
            // 数据类型(看笔记)
            #region
            // 主要见笔记！！！！！
            // 值类型                                          引用类型
            // int, bool, char等                               string Array
            // 方法执行在栈中，所以在方法中声明的变量都在栈中
            // 因为值类型直接存储数据，所以数据存储在栈中
            #endregion
            
            // 声明
            #region
            // 1.声明父类，可以赋值子类（如下的Array是各数组的父类，声明了他，相当于声明了所有类型的数组）
            Array arr1 = new int[2];
            Array arr2 = new string[2];
            Array arr3 = new float[3];
            #endregion
            
            // 特殊数据类型
            #region
            // 所有类的父类：object (他可以声明所有变量，因为是所有类的最高级)
            #region
            object k = 1;
            object k1 = "1";
            object k2 = '1';
            object k3 = new int[] {1, 2, 3, 4};
            #endregion
            // 推断类型：根据所赋数据，推断类型
            #region
            var v1 = "1";
            var v2 = '1';
            var v3 = 1;
            var v4 = false;
            var v5 = 0.1;
            #endregion
            // 字符串池
            #region
            // 字符串常量具备字符串池特性：字符串常量在创建前会先在字符串池中查找是否存在相同文本，如果存在，则直接返回改对象引用，不存在则开辟空间存储(可以提高内存利用率)
            // 字符串具有不可变性(由上方可得)：字符串常量一旦进入内存，就不得改变，因为如果在原位置改变会使其他对象内存被破坏，导致内存泄露，但是遇到字符串变量引用新值时，会在内存新建一个字符串并将此字符串地址交给该变量引用
            // 以下两个新变量s1和s2同为一个字符串
            string s1 = "stupid";
            string s2 = "stubid";
            // 以下两个新变量都为new的字符串，所以所引用的不是同一个字符串
            string s3 = new string(new char[] { 'a', 'b' });
            string s4 = new string(new char[] { 'a', 'b' });
            // 以上验证是否为相同字符串可以用object中的一个方法
            bool r1 = object.ReferenceEquals(s1, s2);
            // 再看一个傻逼操作: 把s1的 "stupid" 改为了 "ass"，注意！这个操作是先在字符串池中找有没有"ass"这个字符串，发现没有后再创建了这个字符串，再把"ass"这个引用重新给了s1，
            s1 = "ass";

            #endregion
            // 可变字符串
            #region
            // 适用性：对字符串的频繁操作
            // 在此使用的是StringBuider这个类，不是一个数据类型，最后输出结果时还要进行ToString
            // 这个特性可以适用于拼接字符串，省内存
            // StringBuider原理：在内存中一次性开辟一块较大的地(取决于后面的容量: 如下方的容量设置为20，一次开辟可以容纳14个字符大小的空间)，在此的每一次修改都是在这一块内存中进行修改从而减少产生的垃圾
            StringBuilder buider = new StringBuilder(20);
            for (int i = 0; i < 14; i++)
            {
                buider.Append(i);
            }
            string result = buider.ToString();
            // 此时可以看到buider中的空间已经满了，但是看下面往buider中继续加入数据还是没有报错
            // 解析：此时buider在内存中开辟了一块更大的地，来储存原先的数据，并且把这个新的引用替换了原来的引用，"蛮不错的" 也加入了buider新的内存地址，从而避免了数据溢出（但是也有一个缺点：之前舍弃的内存地址造成了大量的垃圾）
            buider.Append("蛮不错的");
            // 除此之外，也可以像对字符串对StringBuider类型进行操作
            buider.Insert(0, "草草草");
            buider.Remove(0, 2);
            // 这些操作相对于直接对字符串操作是不一样的，
            string s5 = "12345";
            s5 = s5.Replace('1', '0');  // 这里的Replace必须要接受返回值才能进行操作，如果没有接受返回值是无法对s5进行Replace的，而且同时原来的字符串"12345"也变成了垃圾
            buider.Replace('的', '呢');  // 相对于StringBuider的，StringBuider会直接进行Replace，无需向字符串那样接受返回值，也不会产生新的垃圾
            #endregion

            #endregion

            // 数据类型转换
            #region
            //1.Parse转换：把string转换成其他数据类型，遇到不与转换类型形态相同的转换对象会报错
            string num0 = "18";
            int num1 = int.Parse(num0);
            float num2 = float.Parse(num0);

            //1.5 TryParse转换：与Parse相同的把string转换为其他类型，但是在遇到不与转换类型形态相同的转换对象不会报错，而是返回的结果为false
            string num_1 = "20";
            int result01;
            bool re = int.TryParse(num_1, out result01);
            // 这里使用的输出参数的概念(在传参一部分的笔记中有写到)，此时输出结果：result01 为 20，re 为 true
            
            //2.ToString转换：把任意类型转换成string
            int num3 = 1;
            string num4 = num3.ToString();

            //3.隐式转换：把小范围的转换到大范围（自动转换）
            byte a1 = 100;
            int b1 = a1;

            // 额外知识：对于一个内存块中，不会有空位，如byte类型的一共有八位，假如存储的数字为100，那么内存会被它的二进制数1100100占用但是不满足8位，便在最左侧加上一个0，也就是01100100
            // 第3条隐式转换这里的int类型存储空间大于byte，所以可以直接自动转换，空出的空间用0填充，int有32位，所以除了后面的7位二进制，前面全是0

            //4.显示转换：把大范围的转换到小范围（强制转换），要注意先看一下够不够存储，不然可能会有精度的丢失
            int a2 = 100;
            byte b2 = (byte)a2;
            
            //5.自动类型提升
            byte a3 = 1;
            a3 += 2;   //快捷运算符不会进行类型提升
            a3 = (byte)(a3 + 2);   //byte类型内存容量过小，相加可能会数据溢出，所以会自动提升到int类型，想要正确赋值要显式转换byte
            #endregion

            // 对数据类型的各种常用方法
            #region
            string str = "ass";
            int int1 = 1;
            double d1 = 1;
            string[] strArr = new string[] { "a", "b", "c" };
            bool[] bool0 = new bool[] { true, true, false };
            char[] c1 = new char[3];
            str.Insert(0, "1");  // 在str的索引0位置插入字符串 "1"
            str.ToUpper();  // 转换为大写
            str.ToLower();  // 转换为小写
            str.Substring(1);  // 输出从索引1开始(包括索引1)往后面的字符串，另外一个重载：指定位置（自己看吧。。）
            str.Trim();  // 去除首位的空白字符
            str.Split();

            // 懒得试了。。。
            #endregion
        }

        // 判断语句
        static void Main4()
        {
            // 如果否则语句：一句一句的往下执行，注意里面得else只会与他上面一个的if结合
            #region
            Console.WriteLine("Enter your sex : ");
            string sex = Console.ReadLine();
            if (sex == "man")
            {
                Console.WriteLine("hello, sir");
            }
            else if (sex == "lady")
            {
                Console.WriteLine("hello, madam");
            }
            else
            {
                Console.WriteLine("unkown sex");
            }
            
            #endregion

            // switch语句：会直接根据要判断的值，跳到相应的结果，比如介个sex2如果是woman，他不会一行一行的判断，而是直接跳到第二行进行执行
            #region
            string sex2 = Console.ReadLine();
            string msg;
            switch (sex2)
            {
                //可以使用多个case来表示多个如果的情况，如以下的便是：如果sex2是sir或gentleman或man便进行下面的操作
                case "sir":
                case "gentleman":
                case "man":   //类似于如果否则语句的如果
                    msg = "hello,sir";
                    break;   //记得每一个判断后要加break(打断)来打断case和case的连接
                case "woman":
                case "lady":
                case "madam":
                    msg = "hello,madam";
                    break;
                default:   //类似于如果否则语句的否则
                    msg = "unkown sex";
                    break;
            }
            Console.WriteLine(msg);
            #endregion


            Console.ReadLine();
        }

        // 循环语句
        static void Main5()
        {
            // for循环语句：预定次数循环
            #region
            /*结构
             for (初始化; 循环条件; 增减变量)
             {
                 循环体
             }
            */
            // 执行顺序：先进行初始化(int i=0)，再判断一次(i<5)，满足再进行操作(i++)，再进行判断(i<5)，满足再执行操作(i++)，以此类推
            // 括号中的要素：可以什么都不填(会陷入无限循环)，但是必须要有两个分号，关于条件：可以用bool值的(小心无限循环会死机)
            for (int i = 0; i < 5; i++)
            {
                // 可以使用continue来结束本次循环，开始第二次循环
                if (2 < 1) continue;   //这句的意思便是如果2小于1，那么进行continue操作
                Console.WriteLine("hhh");
            }
            #endregion

            // for for循环（双维数组）
            #region
            // 自己试试看吧，憨批
            Console.WriteLine("你要几层？");
            int a = int.Parse(Console.ReadLine());
            for (int r = 0; r < a; r++)
            {
                for (int c = r + 1; c < a; c++)
                {
                    Console.Write("~");
                }
                Console.WriteLine();
            }
            Console.ReadLine();
            #endregion

            // While循环：相对于do是先判断再循环
            #region
            /*
            while (条件)
            {
                循环体
            }
            */
            #endregion

            // do循环：相对于while是先循环再判断
            #region
            do
            {
                Console.WriteLine("hhh");
            } while (1>2);
            #endregion

            // foreach循环：主要适用于数组，把数组中所有的值输出
            #region
            int[] array = { 1, 2, 3, 4 };
            /*
            foreach (数据类型 变量名 in 数组)
            {
                变量名 即 数组的每一个元素
            }
            */

            foreach (int item in array)
            {
                Console.WriteLine(item);
            }
            #endregion

            // 如何产生随机数
            Random random = new Random();
            random.Next(1, 10);

            Console.ReadLine();
        }

        // 跳转语句
        static void Main6()
        {
            //跳转语句：用于将控制转给另一段代码
            //continue : 退出本次循环进行下次循环
            //break : 退出最近的循环（假如有多个循环嵌套，只退出离自己最近的）；也可以退出swthch语句

            int num = 0;
            while (true)
            {
                num++;
                Console.WriteLine(num);
                if (num <= 5)
                    continue;
                else
                    break;
            }
            Console.ReadLine();
        }

        // 方法(函数)
        #region
        // return：返回值
        
        /* 定义：方法(函数)的语法：  
        [访问 修饰符(级别)] [可选修饰符] 返回类型 方法名称(参数列表)
        {
            方法体
            return 结果
        }  
        */
        // 如下的参数列表中声明了a和b，想要使用Main7这个方法时便必须要得到参数(看下面rest方法中的操作)
        private static int Main7(int a, string b)
        {
            //返回的数据必须与返回值类型相兼容(如上面的返回值类型是int，下面必须用如return 123来返回一个int类型数字)
            //void指的是：没有返回值（下面便可以不用填return），填了return也可以，但是后面不能加数据
            Console.WriteLine(b);
            return 123;
        }
        
        // 调用：
        static void rest()
        {
            int a = 100;
            string b = "hhh";
            //在此想要调用Main7函数必须要先把参数传递给Main7，这个就叫做：传递参数
            Main7(a, b);   //调用Main7这个函数
            //不一定需要用赋值，只要数据类型一样，再传过去就行了
            int num = Main7(100, "hhh");   //把Main7的返回值赋值给num
            Console.WriteLine(num);
        }

        // 方法的 重载 ：方法的名称相同，参数列表不同
        // 作用：在不同条件下，解决同一类问题，调用者只需要记忆一个方法名
        static void a(int a)
        {
            Console.Write(a);
        }
        static void a(int a, int b)
        {
            Console.Write(a + b);
        }
        static void a(int a, int b, string c)
        {
            Console.Write(a + b + c);
        }
        static void final()
        {
            a(1);   //这相当于调用了第一个方法：a
            a(1, 2);   //这相当于调用了第二个方法：a
            a(3, 8, "ddd");   //这相当于调用了第三个方法：a
        }
        //总之这样的话调用的参数更有开放性了


        #endregion

        // 递归算法
        #region
        // 递归：方法内部又调用自身的方法
        // 核心思想：把问题转移给范围缩小的子问题，可以把复杂的问题简单化
        // 弊端：消耗内存较大，性能差（因为每一次进行都要开辟一块空间来存储，到最后再一层一层释放）
        // 一下用计算 3 的阶乘(3*2*1)为例：
        static void Use()
        {
            Console.WriteLine(factorial(3));   //输出了factorial的返回值
            Console.ReadLine();
        }
        static int factorial(int num)
        {
            if (num == 1) return 1;
            return num * factorial(num - 1);
            //返回了的值：num乘以factorial的返回值：重新赋值的num-1(也就是3-1) ，同时也再次调用了自己的这个方法，但是调用的时候参数列表被重新赋值为num-1了(也就是3-1)，然后下面再以num(3-1)乘以factorial的返回值num-1(3-1-1),并返回这个值(2)，同时又起到了调用作用，但是这次调用后因为参数列表的num已经变成了1，所以便返回1，并退出，然后上面便可以输出这些返回值了呢
            //注意：他们是一层一层的返回值，直到最后停止了，返回了1之后，再一层一层还回去，做到阶乘的效果
        }
        #endregion

        // 数组
        #region
        // 一维数组
        static void Main7()
        {
            // 数组的各种写法
            #region
            int[] a;   //初始化数组
            a = new int[6];   //创建新的int类型数组，并设置容量为6
            //  new 数据类型[容量]
            
            // 初始化 + 赋值 （适合已知数组各项的数值使用）
            int[] array1 = new int[3] { 5, 2, 1 };

            // 声明 + 初始化 + 赋值 （这就很他妈简单了）
            int[] array2 = { 1, 2, 3 };
            #endregion

            // 赋值与输出
            #region
            a[0] = 1;   //把1这个值赋值进a这个数组的第一个位置里
            Console.WriteLine(a[0]);   //输出数组a的第一个位置是数值
            #endregion

            // 如何遍历数组
            #region
            // 方法一：
            for (int i=0;i<a.Length;i++)   // .Length是指获取一个数组的长度
            {
                Console.WriteLine(a[i]);
            }
            // 方法二：
            foreach(int item in a)
            {
                Console.WriteLine(item);
            }
            #endregion

            Console.ReadLine();
        }
        // 多维数组
        static void Main8()
        {
            // [行, 列]
            int[,] arr = new int[3, 4];
            arr[0, 0] = 1;
            arr[1, 3] = 2;
            Console.WriteLine(arr[0, 0]);

            // 更加直观的创建方法
            int[,] map = new int[4, 4]
            {
                {2,2,4,8},
                {3,4,5,6},
                {5,6,7,8},
                {6,7,8,9}
            };

            // 遍历多维数组
            // 直接用foreach循环
            foreach (int item in arr)
            {
                Console.WriteLine(item);
            }
            // 用for循环遍历
            // GetLength(0)：获取行数    GetLength(1)：获取列数
            for (int r = 0; r < arr.GetLength(0); r++)
            {
                for (int i = 0; i < arr.GetLength(1); i++)
                {
                    Console.Write("\t");
                    Console.Write(arr[r, i]);
                }
                Console.WriteLine();
            }
        }
        // 交错数组
        private static void Main9()
        {
            // 创建 (绝他妈创建方法，以后就叫他套娃数组了hhhhhhhhh)
            int[][] arr;                    //声明交错数组
            arr = new int[4][];             //创建个有4行(元素)的交错数组
            arr[0] = new int[6];            //创建一个有6个元素的一维数组 赋值给交错数组arr的第一行(元素)
            arr[1] = new int[3];            //创建一个有3个元素的一维数组 赋值给交错数组arr的第二行(元素)
            arr[0][0] = 1;                  //把 1 赋值给arr第1个元素的第1个元素（说人话就是第一行的第一个元素）
            arr[1][2] = 2;                  //把 2 赋值给arr第2个元素的第3个元素

            // 遍历
            foreach (int[] array in arr)
            {
                foreach (int item in array)
                {
                    Console.WriteLine(item);
                }
            }
            
        }
        #endregion

        // params参数数组
        #region
        // 对于方法内部而言就是一个普通数组(各个数组都可以用)
        // 对于方法外部(调用者)而言：可以传递数组，且可以传递一组数据相同的变量集合
        // 接下来是人话：对所有数组都适用，且有了params便可以直接传数据类型相同的参数，甚至可以不传参数，而不需要一个完整的数组
        static int Add(params int[] arr)
        {
            int sum = 0;
            foreach (var item in arr)
            {
                sum += item;
            }
            return sum;
        }
        private static void Params()
        {
            Add(1, 2, 3, 4);
        }
        #endregion

        // 传参
        #region
        static void Main()
        {
            int a = 1;
            ValueParameter(a);
            int a2 = 1;
            ReferenceParameter(ref a2);
            // 输出参数传参前可以不对参数赋值(因为输出参数就是返回个结果，所以赋值没有意义)
            int a3;
            OutputParameter(out a3);

        }
        
        // 值参数
        static void ValueParameter(int a)
        {
            // 按值传递 -- 传递实参变量储存的内容
            // 作用：传递信息
            a = 2;
        }
        
        // 引用参数(引用参数前加 ref )
        static void ReferenceParameter(ref int a)
        {
            // 按引用传递 -- 传递实参变量自身的内存地址
            // 作用：改变数据
            a = 2;
        }
        
        // 输出参数(引用参数前加 out )
        static void OutputParameter(out int a)
        {
            // 按引用传递 -- 传递实参变量的内存地址
            // 作用：返回结果
            // 与引用参数区别：1. 方法内部必须为输出参数赋值(如下方必须对 a 赋值)    2. 
            a = 2;
        }
        #endregion

        // 变量
        #region
        // 局部变量
        // 定义在方法内部的变量叫局部变量

        // 成员变量
        // 定义在类中、方法外的变量叫成员变量
        // 特点：
        // 1.具有默认值(声明之后便可以直接使用)    
        // 2.所在的类被实例化后，存在堆中，对象被回收时，成员变量从堆中清除    
        // 3.可以与局部变量重名(使用在类中的成员变量时，要使用 this )
        #endregion

        // 简单枚举
        #region
        // 解析：列举某种数据的所有取值，可以增强代码的可读性，限定取值
        // 以下以上下左右的移动举例
        // 如果不使用枚举，那么对上下左右的方法调用的时候就要记忆四种方法名称比如MoveUp(), MoveDown(), MoveLeft(), MoveRight()十分麻烦(万一有更多的就草了)
        // 枚举默认类型为int  数据类型：int             数据：1 2 3 4
        //                   数据类型：MoveDirection   数据：MoveDirection.Up  MoveDirection.Down ......
        static void MoveUp()
        {

        }
        static void MoveDown()
        {

        }
        static void MoveLeft()
        {

        }
        static void MoveRight()
        {

        }
        private static void Move(MoveDirection direction)
        {
            switch (direction)
            {
                case MoveDirection.Up:
                    MoveUp();
                    break;
                case MoveDirection.Down:
                    MoveDown();
                    break;
                case MoveDirection.Left:
                    MoveLeft();
                    break;
                case MoveDirection.Right:
                    MoveRight();
                    break;
            }
        }
        private static void Use1()
        {
            // 此时便可以更方便的调用
            Move(MoveDirection.Down);
        }
        #endregion

        // 调用多个枚举
        #region
        private static void Main10()
        {
            //0000000001 | 0000000010  -->  0000000011
            PrintPersonStyle(PersonStyle.stupid | PersonStyle.ass);

            // 数据类型转换
            // int  -->  Enum
            PersonStyle style01 = (PersonStyle)2;
            // Enum  -->  int
            int enumNumber = (int)(PersonStyle.stupid);
            // string  -->  Enum
            PersonStyle style02 =
                (PersonStyle)Enum.Parse(typeof(PersonStyle), "stupid");
            // Enum  -->  string
            string enumStr = PersonStyle.shitty.ToString();
        }
        private static void PrintPersonStyle(PersonStyle style)
        {
            // 判断是否包含
            if ((style & PersonStyle.stupid) == PersonStyle.stupid) Console.WriteLine("stupid");
            if ((style & PersonStyle.shitty) != 0) Console.WriteLine("shitty");
            if ((style & PersonStyle.fucking) != 0) Console.WriteLine("fucking");
            if ((style & PersonStyle.cocky) == PersonStyle.cocky) Console.WriteLine("cocky");
            if ((style & PersonStyle.ass) != 0) Console.WriteLine("ass");
        }
        #endregion

        // 类和对象
        #region
        // 类：指一个类别(抽象的概念)
        // 对象：一个具体的对象
        // 目前已定义萝莉这个类(具体见类和对象笔记)
        static void Main11()
        {
            // 在栈中声明 Loli 类型的引用
            Loli loli01;
            // 指向 Loli 类型的对象(实例化 Loli 类型对象)，在堆中开辟了 loli01 并包含6个内存块(name, age, sex, ageIncrease, 类型同步对象指针, 同步快索引)因为Loli这个类中创建了前四个变量
            loli01 = new Loli();
            loli01.SetName("Sylive");
            loli01.SetAge(11);
            loli01.AgeIncrease(false);
        }
        // 具体看 类和对象笔记 这个文件！！！！！！
        #endregion


    }

}
