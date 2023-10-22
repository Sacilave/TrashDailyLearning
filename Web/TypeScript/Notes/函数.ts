/*语法
 function 函数名(参数列表): 数据类型
 {
     函数体
 }
 可以不填函数的数据类型，默认为 void
 调用: 函数名(参数列表)
 ps: 调用的时候所给的参数叫 实参 , 函数所要的参数叫形参，调用时实参赋值给形参
 */

 function getSum(numArr: number[]): number
{
    let sum: number = 0;
    for(let i: number = 0; i<numArr.length; i++)
    {
        sum += numArr[i];
    }
    return sum;
}
console.log(getSum([1,2,4,7,6,7,9,7,7,8]))

// 回调函数
function forEach01(callbackfn: (item: string, index: number) => void)
{ 

}
// 调用时不需要再对参数(这个方法)添加类型注解，因为是传递实参，当前的方法 fff 的类型注解相当于之前定义的方法里的参数的注解: void （所以有无名称不重要）
forEach01(function fff(itemV, indexV){ console.log(itemV, indexV) })
// 那么为什么要这样：把一个方法作为参数传递进被调用的方法中呢 -- 如果把上面方法的 item 的类型改成 boolean 那么下面的 itemV 的类型也会变成boolean
// 这样会形成：传递 fff 这个函数参数的时候必须传递一个 forEach01 中所指定的参数类型
// 所以再看看forEach函数
let str00: string[] = ['a','b', 'c', 'd']
str00.forEach(function(value){console.log(value)})  // 此时的 value 便为string类型
let str11: number[] = [0, 1, 2, 3, 4]
str11.forEach(function(value){console.log(value)})  // 此时的 value 便为number类型
// forEach() 可以根据回调函数类型自动推断出类型

