using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace day2
{
    /// <summary>
    /// 定义 萝莉 类
    /// </summary>
    class LovelyLoli
    {
        
    }
    class Loli
    {
        // 数据成员
        private string name;

        private string sex;  // 草(为什么还有sex这种数据成员啊啊啊啊啊啊)

        private int age;

        private bool ageIncrease;

        // 字段与属性
        #region
        // 字段：存储数据
        // private string name;
        // 属性(本质就是两个方法，对字段的读取和写入)：保护字段，可以实现对字段的只读和只写功能
        public string Name
        {
            // 读取时保护
            get
            { return name; }
            // 写入时保护(value: 要设置的数据)
            set
            { this.name = value; }
        }
        public int Age
        {
            get
            { return age; }
            set
            {
                if (value < 18)
                    this.age = value;
                else
                    throw new Exception("这他妈是萝莉？？");
            }
        }
        // 调用
        static void Main0()
        {
            Loli loli02 = new Loli();
            loli02.Name = "Sylvie";  // 相当于执行了 set 代码块
            Console.WriteLine(loli02.Name);  // 相当于执行了 get 代码块
        }
        #endregion

        // 构造函数
        #region
        /* 
        构造函数：提供了创建对象的方式，常常用于初始化类的数据成员
         * 特点：没有返回值，与类同名 创建对象(new)时自动调用(不能被手动调用)
         * 本质：方法
         * 一个类若没有构造函数，那么编译器会自动提供一个无参数构造函数
         * 一个类若有构造函数，那么编译器不会自动提供无参数构造函数
         * 如果不希望在类的外部被创建对象，就将构造函数私有化(将访问修饰符换成 private )
        */
        public Loli()
        {
            Console.WriteLine("已创建");
            // 顺便一提：构造函数也可以重载呢
        }
        public Loli(string name):this()  // :this 指的是调用 Loli() 这个构造函数(这是唯一的一个调用构造函数的方法)
        {
            this.Name = name;  // 构造函数如果为字段赋值，属性中的代码块不会执行(要根据实际需求决定是用属性还是直接使用代码块)
        }
        public Loli(string name, int age):this(name)  // :this(name) 指的是调用 Loli(string name) 这个构造函数
        {
            this.Age = age;
        }
        
        static void Main1()
        {
            Loli loli03 = new Loli("vanilla", 11);
        }
        #endregion

        // 方法成员
        public void SetName(string name)
        {
            // this 指的是这个对象(引用)，在此的 this.name 就是指name这个对象的引用
            // 在调用这个函数的时候获取参数后赋值给 name 对象的内存地址所指向的数据，也就是上面声明的四个变量(name, sex, age, ageIncrease)中的 name 变量
            this.name = name;
        }
        public void SetAge(int age)
        {
            this.age = age;
        }
        public void AgeIncrease(bool ageIncrease)
        {
            this.ageIncrease = ageIncrease;
        }
        public string GetName()
        {
            return this.name;
        }
        public int GetAge()
        {
            return this.age;
        }
        
    }
}
