using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TouchTest : MonoBehaviour
{
    void Start()
    {
        Input.multiTouchEnabled = true;  // 开启多点触摸
    }

    void Update()
    {
        // 判断单点触摸
        if (Input.touchCount == 1)  // 判断触摸点为 1 个
        {
            // 触摸对象
            Touch touch = Input.touches[0];  // 触摸为一个列表类型，因为是单点触摸，所以取第一个元素
            // 触摸位置
            Debug.Log(touch.position);
            // 触摸阶段
            switch (touch.phase)
            {
                case TouchPhase.Began:
                    break;
                case TouchPhase.Moved:
                    break;
                case TouchPhase.Stationary: 
                    break;
                case TouchPhase.Ended:
                    break;
                case TouchPhase.Canceled:
                    break;
            }
        }

        // 判断多点触摸
        if (Input.touchCount == 2)  // 判断触摸点有 2 个
        {
            Touch touch = Input.touches[0];
            Touch touch1 = Input.touches[1];  // 有几个 触摸点，即有几个触摸元素
        }
    }
}
