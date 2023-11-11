using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DebugTest : MonoBehaviour
{
    // 以下全部用于 Debug
    void Start()
    {
        Debug.Log("normal message");
        Debug.LogWarning("Warning message");
        Debug.LogError("Error message");
        
    }

    // Update is called once per frame
    void Update()
    {
        Debug.DrawLine(Vector3.zero, Vector3.one, Color.red);  // 画一条线 (起点，终点)
        Debug.DrawRay(Vector3.zero, Vector3.up, Color.blue);  // 绘制射线 (起点，射线)
    }
}
