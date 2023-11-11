using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Vector : MonoBehaviour
{
    void Start()
    {
        // 向量，坐标，旋转，缩放
        Vector3 v = new Vector3 (0, 0, 0);
        v = Vector3.zero; // (0,0,0)
        v = Vector3.one;

        Vector3 v2 = Vector3.forward;

        // 计算两个向量夹角
        Debug.Log(Vector3.Angle(v, v2));
        // 两点距离
        Debug.Log(Vector3.Distance(v, v2));
        // 点乘 (向量相乘，结果为 点积 又称 数量积 或 标量积)，反映了两个向量在方向上的相似度，越大越相似
        Vector3.Dot(v, v2);
        // 叉乘 如果两向量构成平行四边形，向量叉乘结果等于这个平行四边形面积
        Vector3.Cross(v, v2);
        // 插值
        Vector3.Lerp(v, v2, 0.8f);
        // 向量的模
        Debug.Log(v.magnitude);
        // 规范化向量
        Debug.Log(v.normalized);
    }

    void Update()
    {
        
    }
}
