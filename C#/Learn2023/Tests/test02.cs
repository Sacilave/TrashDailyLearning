#define PI
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;



namespace Tests
{
    
    class testA
    {
        public static void Main()
        {
            FileStream f = new FileStream("D:\\TECH\\C#\\Learn2023\\Notes\\Notes\\Notes.txt", FileMode.Open, FileAccess.Read, FileShare.Read); 
            Console.WriteLine(f.ToString());
        }
    }
}
namespace Test01
{
    namespace test02
    {
        class A
        {
            public static void output()
            {
                Console.WriteLine("abab");
            }
        }
    }
}
