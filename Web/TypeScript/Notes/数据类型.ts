// 数据类型

/*原始类型 (基本数据类型)
    布尔类型   (boolean)
    数字类型   (number)
    字符串类型 (string)
    null 和 undefined
    void类型

  对象类型 (复杂数据类型)
    数组类型   (array)
    元组类型   (couple)
    枚举类型   (menu)
    任意类型   (any)
    never类型
*/

// TYPE: number
    let num0: number;  
    num0 = 2;  // 可为整数
    let num1: number;
    num1 = 2.3;  // 可为小数
    let num2: number;
    num2 = -2;  // 可为负数

// TYPE: string
    let str0: string;
    str0 = "a";
    let str1: string;
    str1 = 'a';  // 也可使用单引号(没区别)

// TYPE: boolean
    let bool0: boolean;
    bool0 = true;

// TYPE: undifined -- 声明了变量，没有值(就好比根本没有纸，连纸筒也没有)
    let undefined0: undefined = undefined;

// TYPE: null -- 声明了变量，值为 null (就好比纸用完了就剩下一个纸筒)
    let null0: null = null;


// 类型注解
    // 对于一个对象需要进行类型注解
    let hhh: string;  //这里的 hhh 的类型注解就是string
    let gggii: () => void  //这里 gggii 的类型注解是 () , 意思是 方法 , 是个 void 类型的方法
    let iiigg: () => number  //这里 iiigg 的类型注解也是 () , 意思也是 方法 , 是个 number 类型的方法
    
    // 在有些情况下可以不写类型注解 -- 这种情况叫做 类型推论
    // 最常发生 类型推论 有两种情况     
    
    // 1.声明变量并初始化时
        let testA = 1;  // 直接赋值没毛病，此时可以发现 testA 的类型推论为 number
        let testB = 'awsl';  // 此时可以发现 testB 的类型推论为 string
        
        let testC;  // 但是这种情况就不一样了
        testC = 1;  // 先声明后赋值，而不是直接在声明的同时赋值，这会导致他的类型推断变为 any 类型
        testC = 'cao'  // 不过既然成了 any 类型，也可以随便赋值了呢(虽然说对内存消耗很大就对了)

    // 2.决定函数的返回值时
        function fun1(num01: number, num02: number)
        {
            return num01+num02
        }
        // 此时并没有增加类型注解，但是可以看到 fun1 的类型为 number 类型
