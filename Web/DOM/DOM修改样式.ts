// 使用DOM操作样式
let p = document.querySelector("#paragraph") as HTMLParagraphElement
let p2 = document.querySelector("#paragraph2") as HTMLParagraphElement
// style属性 (行内样式)
    p.style.color = 'green'
    p.style.fontSize = '50px'
    p2.style.display = 'none'  // 隐藏元素
    p2.style.display = 'block'  // 显示元素

// classList属性 (类样式)
    // 包含三个常用操作：添加、移除、判断是否存在
    p.classList.add('a', 'b', 'c')  // 添加类名
    p.classList.remove('c')  // 移除类名
    let has = p.classList.contains('a')  // 判断是否存在类名