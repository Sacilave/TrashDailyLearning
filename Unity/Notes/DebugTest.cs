using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DebugTest : MonoBehaviour
{
    // ����ȫ������ Debug
    void Start()
    {
        Debug.Log("normal message");
        Debug.LogWarning("Warning message");
        Debug.LogError("Error message");
        
    }

    // Update is called once per frame
    void Update()
    {
        Debug.DrawLine(Vector3.zero, Vector3.one, Color.red);  // ��һ���� (��㣬�յ�)
        Debug.DrawRay(Vector3.zero, Vector3.up, Color.blue);  // �������� (��㣬����)
    }
}
