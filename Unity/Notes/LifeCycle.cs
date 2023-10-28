using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LifeCycle : MonoBehaviour
{
    /* 脚本的生命周期
    Awake()  最早调用，可以使用单例模式
    OnEnable()  组件激活后调用一次，Awake() 调用后自动调用一次，不用于值的初始化
    Start()  在 Update 之前调用一次，可以用于设置初始值
    FixedUpdate()  固定频率调用，时间间隔相同，默认0.02s。可在 U3d 中修改：Edit, Project Settings, Time, Fixed Timestep 中修改
    Update()  每帧调用一次
    LateUpdate()  每次 Update() 调用完后被调用
    OnDisable()  组件未激活时调用
    OnDestroy()  组件被销毁后调用一次
     */

    void Awake()
    {
        Debug.Log("Awake function enabled");  // 输出
    }
    void Start()
    {
        
    }
    void Update()
    {
        
    }
    void FixedUpdate()
    {
        // Debug.Log("FixedUpdate() enabled, frequency 0.02s");
    }
}
