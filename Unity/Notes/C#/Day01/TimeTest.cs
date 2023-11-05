using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TimeTest : MonoBehaviour
{
    float timer = 0;
    void Start()
    {
        // 游戏开始到现在的时间
        Debug.Log(Time.time);
        // 时间缩放值
        Debug.Log(Time.timeScale);  // 可用于控制时间的加速减速
        // 固定时间间隔
        Debug.Log(Time.fixedDeltaTime);
    }

    void Update()
    {
        // 上一帧到这一帧所用的时间
        Debug.Log(Time.deltaTime);  // 可用于制作计时器
        timer += Time.deltaTime;
    }
}
