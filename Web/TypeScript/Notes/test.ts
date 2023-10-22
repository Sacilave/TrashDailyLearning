let a: number[] = [0,3,5,6,4,6,3,9,11,65,11,3,8,9,14,8,13]
let count: number = null
a.forEach
(
    function(value)
    {
        if(value>10)
        {
            console.log(value)
            count++
        }
    }
)
console.log("共有", count, "个数大于10")