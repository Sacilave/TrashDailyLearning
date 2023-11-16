using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TransformTest : MonoBehaviour
{
    void Start()
    {
        // 输出位置 (均为 Vector3 类型)
        Debug.Log(transform.position);  // 相对世界而言
        Debug.Log(transform.localPosition);  // local 是相对于父物体而言

        // 获取旋转 (四元数类型)
        Debug.Log(transform.rotation);
        Debug.Log(transform.localRotation);
        // 获取旋转 (欧拉角类型，也就是 Vector3)
        Debug.Log(transform.eulerAngles);
        Debug.Log(transform.localEulerAngles);

        // 获取缩放
        Debug.Log(transform.localScale);

        // 获取方向向量
        Debug.Log(transform.forward);  // x 轴
        Debug.Log(transform.right);  // z 轴
        Debug.Log(transform.up);  // y 轴


        // 父子关系
        GameObject go01 = transform.parent.gameObject;  // 获取父物体
        int childNum = transform.childCount;  // 子物体个数
        transform.DetachChildren();  // 脱离与子物体关系：
        Transform trans = transform.Find("Child");  // 获取子物体通过名称
        Transform trans02 = transform.GetChild(0);  // 获取子物体通过索引
        bool res = trans.IsChildOf(transform);  // 判断一个物体是不是另一个物体的子物体
        trans.SetParent(transform);  // 将 trans 设置为 此物体的父物体
    }

    void Update()
    {
        transform.LookAt(Vector3.zero);  // 看向一个点
        transform.Rotate(Vector3.up, 1);  // 自转 1°
        transform.RotateAround(Vector3.zero, Vector3.up, 5);  // (绕的点，绕的轴，旋转速度)
        transform.Translate(Vector3.forward * 0.1f);  // 移动
    }
}
