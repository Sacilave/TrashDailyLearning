string friendName = "Steve";
string spaceValue = "           abab     ababsjdfbjs  bafsbfjsadbkf     ";

#region
// 字符串

// Console 类属于 System 文件中，但不使用 Using System; 直接调用 Console 时，调试器会自动调用
Console.WriteLine($"ur friend name is : {friendName}, the length is {friendName.Length}");  // 字符串内插：使用 $" {变量名} " 格式进行字符串内插操作。.Length 可获取字符串长度，Length 是字符串类型

Console.WriteLine($"{spaceValue}");
// Trim 函数可以删除字符串前和后的空格，TrimStart 和 TrimEnd 分别删除前和后的空格
string spaceValue1 = spaceValue.Trim();  // 在对字符串操作时需要重新赋值而不是直接修改

//  Replace 函数可以替换字符串
friendName = friendName.Replace("S", "A");

// 分别为 转大写 和 转小写
Console.WriteLine(friendName.ToUpper());
Console.WriteLine(friendName.ToLower());

// Contains 函数判断字符串是否存在，返回值为 true 或 false，但作为字符串输出时输出 True 和 False
Console.WriteLine(spaceValue.Contains("abab"));

// StartsWith 和 EndsWith 分别判断开头与结尾是否存在字符串，输出与 Contains 函数相同
Console.WriteLine(friendName.StartsWith("St"));

#endregion

#region
// 数字
/*
 * int
 * float
 * double
 * decimal
 * 
 */
// 获取类型的限度
Console.WriteLine(double.MaxValue);
Console.WriteLine(double.MinValue);
Console.WriteLine(decimal.MaxValue);
Console.WriteLine(decimal.MinValue);

#endregion

#region
// 列表

// 创建列表 使用 var 列表名 = new List<列表类型> {"","",""}
var names = new List<string> { "Steve", "Lave" };
// 列表 添加 和 删除 ：列表名.Add(值)  列表名.Remove(值)
names.Add("Tom");  names.Remove("Steve");
// 获取列表长度用 列表名.Count
Console.WriteLine(names.Count);
// 列表查找返回索引值使用 列表名.IndexOf(值)  返回值为此项的索引值，不存在则返回 -1
foreach (string name in names)
{
    Console.WriteLine(names.IndexOf(name));
}  // 如此可输出列表内所有元素的索引
// 列表排序：使用 列表名.Sort()  如果为 String 类型列表 则按照字母顺序排序

#endregion