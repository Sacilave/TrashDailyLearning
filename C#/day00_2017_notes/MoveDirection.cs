using System;
namespace Move
{
    /// <summary>
    /// 定义枚举类型：移动方向
    /// </summary>
    enum MoveDirection : int  // 定义MoveDirection的类型为int(除此之外可以使用其他常用类型比如byte, long, string)
    {
        // 创建语法：enum 枚举名 {}
        // 以下对创建的数据类型定义值
        Up = 0,
        Down = 1,
        Left = 2,
        Right = 3
    }
}
