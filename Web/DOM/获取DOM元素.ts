/*获取一个 DOM元素
    document.querySelector(selector)
    document(对象): 文档对象(整个页面)，是操作页面内容的入口对象
    selector(参数): 是一个CSS选择器(标签、类、id 选择器等)
    作用：可以获取与选择器参数匹配的DOM元素，但是只能获取第一个！！！！(注意！只能获取第一个)
    所以推荐使用 id选择器
*/
    // 获取id为 title 的 DOM元素
    let titleDOM = document.querySelector("#title")
    console.log(titleDOM)

/*获取多个 DOM元素
    document.querySelectorAll(selector)
    与上方获取一个DOM元素的 querySelector 相同
    但是！！这个可以获取所有与选择器匹配的元素
    返回值时一个列表！！
    所以推荐使用 class 选择器
*/
    // 获取 class 名为 cls 的 DOM元素
    let titleDOM00 = document.querySelectorAll(".cls")