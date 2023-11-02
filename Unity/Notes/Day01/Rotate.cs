using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotate : MonoBehaviour
{
    void Start()
    {
        // 旋转：使用 欧拉角 或 四元数
        Vector3 rotateEuler = new Vector3(0, 30, 0);  // 新建一个 y轴 旋转30度的三维坐标变量
        Quaternion rotateQuaternion = Quaternion.identity;  // 新建一个 四元数变量 
        // 欧拉角转为四元数
        rotateQuaternion = Quaternion.Euler(rotateEuler);
        // 四元数转化为欧拉角
        rotateEuler = rotateQuaternion.eulerAngles;
        // 看向一个物体来旋转
        rotateQuaternion = Quaternion.LookRotation(new Vector3(0, 0, 0));  // 看向了新建的一个三维向量
    }

    void Update()
    {
        
    }
}
