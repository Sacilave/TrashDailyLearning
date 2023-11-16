using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AxisTest : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        float horizontal = Input.GetAxis("Horizontal");
        Input.GetButtonDown("Jump");  // 同时也具有 GetButton, GetButtonUp 方法，在 Project Settings，Input Manager 中有各类虚拟轴和虚拟按键的定义
    }
}
