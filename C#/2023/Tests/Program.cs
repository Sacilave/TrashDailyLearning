using System.Runtime;

namespace test01
{
    class tests
    {
        static void output()
        {
            for (int i = 0; i < 12; i++)
            {
                Console.Write("*");
            }
            Console.WriteLine("\nWelcome");
            for (int i = 0; i < 12; i++)
            {
                Console.Write("*");
            }
        }
        static void calculateSquare()
        {
            Console.WriteLine("输入矩形的长");
            float length = float.Parse(Console.ReadLine());
            Console.WriteLine("输入矩形的宽");
            float width = float.Parse(Console.ReadLine());
            Console.WriteLine($"周长为：{Math.Round(2 * length * width, 2)}，面积为：{Math.Round(length * width, 2)}");
        }
        static void getMinL()
        {
            static int getMin(int a, int b)
            {
                if (a < b) return a;
                else return b;
            }
            Console.WriteLine("输入第一个数");
            int num01 = int.Parse(Console.ReadLine());
            Console.WriteLine("输入第二个数");
            int num02 = int.Parse(Console.ReadLine());
            Console.WriteLine("输入第三个数");
            int num03 = int.Parse(Console.ReadLine());
            Console.WriteLine($"最小数为：{getMin(getMin(num01, num02), num03)}");
        }
        static void NarcissisticNum()
        {
            Console.WriteLine("输入一个数: ");
            double sum01 = 0;
            int numIn = int.Parse( Console.ReadLine() );
            int[] arr = new int[numIn.ToString().Length];
            int tmp = numIn;
            for(int i = numIn.ToString().Length; i != 0; i--)
            {
                arr[i-1] = numIn % 10;
                numIn /= 10;
            }
            for (int i = 0; i < arr.Length; i++) sum01 += Math.Pow(arr[i], 3);
            if ((sum01 - tmp) == 0) Console.WriteLine("是个水仙花数");
            else Console.WriteLine("不是水仙花数");
        }
        static void unrepeat()
        {
            int[] arr = { 1, 2, 3, 4 };
            int res = 0;
            for (int i = 0; i<arr.Length; i++)
            {
                for (int j = 0; j<arr.Length; j++)
                {
                    for(int h = 0; h<arr.Length; h++)
                    {
                        Console.WriteLine($"{arr[i] * 100 + arr[j] * 10 + arr[h]}");
                        res++;
                    }
                }
            }
            Console.WriteLine($"共可组成 {res} 个数字");
        }
        static void fish()
        {
            static int fishDivide(int num)
            {
                return num * 5 + 1;
            }
            Console.WriteLine(fishDivide(fishDivide(fishDivide(fishDivide(6)))));
        }
        static void issue07()
        {
            int numIn = int.Parse(Console.ReadLine());
            bool flag = true;
            int i = 2;
            while(i < numIn-1){
                if (numIn%i == 0)
                {
                    flag = false;
                }
                i++;
            }
            switch (flag)
            {
                case false: Console.WriteLine("不是素数"); break;
                case true: Console.WriteLine("是素数"); break;
            }
        }
        static void backNum()
        {
            Console.WriteLine("输入一个数判断是否为回文数");
            int numIn = int.Parse(Console.ReadLine()); int tmp = numIn;
            int[] arr = new int[numIn.ToString().Length];
            bool flag = true;
            for (int i = numIn.ToString().Length; i != 0; i--)
            {
                arr[i-1] = tmp%10;
                tmp /= 10;
            }
            for (int i = 0; i < numIn.ToString().Length / 2 + 1; i++)
            {
                if (arr[i] != arr[numIn.ToString().Length-i-1])
                {
                    flag = false;
                }
            }
            switch (flag)
            {
                case false: Console.WriteLine("不是回文数"); break;
                case true : Console.WriteLine("是回文数"); break;
            }
        }
        static void test()
        {
            int[] arr = new int[6];

            foreach(int item in arr)
            {
                Console.WriteLine(arr.Length);
            }
        }
        static void Main()
        {
            
        }
    }
}