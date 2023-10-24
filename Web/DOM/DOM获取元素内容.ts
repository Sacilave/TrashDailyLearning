// 使用TEST.html举例

// 获取 id 为title的文本内容
let title = document.querySelector('#title') as HTMLHeadingElement  // 使用 innerText 必须要对对象添加类型断言 
console.log(title.innerText)

// 设置 id 为title的内容
title.innerText = "绝他妈的"
console.log(title.innerText)

// 追加内容
title.innerText += "蛮不错的"
console.log(title.innerText)