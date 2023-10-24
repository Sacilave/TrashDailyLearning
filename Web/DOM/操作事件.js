// 像点击鼠标，敲击键盘等功能要靠操作事件来实现，其实这些都是常见的DOM事件
var btn = document.querySelector("#btn");
var btn2 = document.querySelector("#btn2");
var btn3 = document.querySelector("#btn3");
var p = document.querySelector("#paragraph2");
// 添加事件：addEventListener(事件名称, 事件处理程序)
btn.addEventListener('mouseenter', function (event) {
    console.log("鼠标移入了");
    console.log(event.type);
    console.log(event.target);
});
// 事件对象(event)：是 事件处理程序(回调函数) 的参数
// 表示：与当前事件相关的信息，比如：事件类型(type)、触发事件的DOM元素 (target) 等
// 整个示例：按下按钮使按钮变成30px
btn.addEventListener('click', function (event) {
    var eventTarget = event.target;
    var random = Math.floor(Math.random() * 30) + 10; // 这是生成随机数的方法(生成1~29的数字)
    eventTarget.style.fontSize = random + 'px';
    console.log("鼠标点击了");
});
// 移除事件：removeEventListener(事件名称, 事件处理程序)
// 作用：移除给DOM元素添加的事件，移除后，事件就不再触发了
// 注意！事件处理程序 必须要跟添加事件时的事件处理程序是同一个！！！否则无法删除！！！
// 于是！正确的写法就出现了。。呢。。。(妈耶。。现在看着右下角的live2d为什么这么寂寞呢。。。)
function noneClick() { }
btn.removeEventListener('click', noneClick);
btn.removeEventListener('click', noneClick);
// 现在做一个点击 "移除点击事件" 按钮后移除 "移除" 按钮的功能
function handleClick() {
    console.log("被点击了呢");
}
btn2.addEventListener('click', handleClick);
btn3.addEventListener('click', function () {
    btn2.removeEventListener('click', handleClick);
});
// 如果该事件仅需要触发一次，可以在添加事件时处理：传入第三个参数{once:true}
btn3.addEventListener('mouseenter', function () { console.log("鼠标移入了"); }, { once: true });
