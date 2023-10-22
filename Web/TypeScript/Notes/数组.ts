// 创建
    let arr0: string[];
    arr0 = []  // 创建一个空数组
    arr0 = ['shit', 'ass', 'trash', 'rubbish']
    // 除此之外也可以用 new Array()
    let arr1: string[] = new Array('shit', 'shit', 'shit')

// 长度(没错还是用length)
    console.log(arr0.length)

// 索引(嘛，跟其他语言差不多)
    console.log(arr0[0])

// 添值(在TS中若果所用的索引不存在则自动添加值)
    arr0[4] = 'deep'
    // 那么一个天才的添加方法就出现了(在末尾添加新元素的方法)
    arr0[arr0.length] = 'dark'
    arr0[arr0.length] = 'nice'

// 遍历
    let tArr: string[] = ['a','b', 'c', 'd']
    for(let i: number = 0; i<tArr.length; i++)
    {
        console.log(tArr[i])
    }

// 另外还可以使用 forEach 遍历(! ！ 适用于对所有项的全部遍历 ！！)
    tArr.forEach( function(item,index) { console.log('索引为', index, '元素为', item) } )
    
// 使用 some 方法遍历 -- some 遍历数组，查找是否有一个满足条件的元素(如果有，立即停止循环)
    tArr.some(function bbb(value)
    {
        if (value === 'c')
        {
            return true
        }
        return false
    })
    // 特点：根据回调函数(在这里就是bbb)的返回值决定是否停止循环：如果为true就停止，为false则继续
