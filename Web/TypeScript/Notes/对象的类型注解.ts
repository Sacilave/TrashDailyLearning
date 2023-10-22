// TS中的对象是结构化的(结构简单来说就是对象有什么属性或方法)
// 在使用对象前可以根据需求提前设计好一个结构
// 举例 （该结构类似于C#中的构造函数）
let loli00:  // 类型注解(使用冒号结束)
{
    name: string;  // 这个是对 属性 的类型注解
    speak: () => string;  //这个是对 方法 的类型注解
}

loli00 =   // 对象(使用逗号结束)
{
    name: "Sylvie",
    speak()
    {
        return "hentai, this is Sylvie"
    },
}
