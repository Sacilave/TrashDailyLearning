// 取值
    let loli = 
    {
        name: "Sagiri",
        age: 12,
        say:function()
        {
            console.log("This is Sagiri")
        }
    }
    // 取值：拿到对象中的属性或方法并使用
    // 获取对象中的属性，称为：访问属性 -- 使用 . 进行访问(看见了吗，是个点！)
    console.log(loli.name)
    // 获取对象中的方法并调用，称为：调用方法
    loli.say()

// 存值
    loli.name = "Sagiri!!!"
    loli.age = 13
    // 就直接重新赋值。。。
    // 方法基本不会二次修改