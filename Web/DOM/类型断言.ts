// 如果直接获取指定的元素并赋值会发现被赋值的变量默认就是 Element(元素)类型，这会让后面分不清每个元素
let titleDOM3 = document.querySelector("#title")
let imgDOM3 = document.querySelector("#img")

// 所以应该添加类型断言（在后面使用 as 语句并添加类型）
let titleDOM2 = document.querySelector("#title2") as HTMLHeadingElement
let imgDOM2 = document.querySelector("#img2") as HTMLImageElement

// 对于每个类型断言是不一样的可以使用一个神奇的命令
console.dir(titleDOM2)  // 比如这个可以获取titleDOM2的类型了