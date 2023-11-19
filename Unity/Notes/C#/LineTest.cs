using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LineTest : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        // 设点线段位置
        LineRenderer lineRenderer = GetComponent<LineRenderer>();
        lineRenderer.positionCount = 3;  // 设置Line的锚点个数
        lineRenderer.SetPosition(0, Vector3.zero);  // 设置单个点的位置 (第 0 个，位置)，可以使用 SetPositions() 设置多个点的位置，参数为一个数组，数组元素分别对应各个点的位置
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
