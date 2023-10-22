// 因为直接在对象名称后面写类型注解会不简洁，而且无法复用类型注解，所以可以使用 接口(interface)
// 接口：为对象的类型注解命名，并为代码建立契约来约束对象的结构
/*语法
 interface 接口名
 {
     属性
 } 
 */
interface loli001
{
    name: string;
    age: number;
    say: () => void;
}
// 使用
let p1: loli001 =
{
    name: "neko",
    age: 11,
    say()
    {
        return
    }
}
// 接口可多次使用
let p2: loli001 =
{
    name: "neeko",
    age: 12,
    say()
    {
        return
    }
}