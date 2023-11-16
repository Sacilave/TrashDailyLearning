using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class KeyTest : MonoBehaviour
{
    void Start()
    {
        
    }

    void Update()
    {
        // 鼠标的点击
        // 按下鼠标 0左键  1右键  2滚轮
        if (Input.GetMouseButtonDown(0)) { }
        // 持续按下鼠标
        if (Input.GetMouseButton(0)) { }
        // 抬起鼠标
        if (Input.GetMouseButtonUp(0)) { }

        // 键盘按键
        // 按下键盘按键
        if (Input.GetKeyDown(KeyCode.Space));  // KeyCode 为枚举类型，也可使用字符比如 "a"，不区分大小写
        // 持续按下键盘
        Input.GetKey(KeyCode.K);
        // 松开键盘按键
        Input.GetKeyUp(KeyCode.Space);
    }
}
