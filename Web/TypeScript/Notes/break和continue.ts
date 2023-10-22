// break 表示直接跳出循环
for(let i: number = 1; i<=5; i++)
{
    if(i === 3)
    {
        break
    }
    console.log("第", i, "次循环")
}

// continue 表示跳过本次循环直接进行下一次循环
for(let i: number = 1; i<5; i++)
{
    if(i === 3)
    {
        continue
    }
    console.log("第", i, "次循环")
}

