using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Vector : MonoBehaviour
{
    void Start()
    {
        // ���������꣬��ת������
        Vector3 v = new Vector3 (0, 0, 0);
        v = Vector3.zero; // (0,0,0)
        v = Vector3.one;

        Vector3 v2 = Vector3.forward;

        // �������������н�
        Debug.Log(Vector3.Angle(v, v2));
        // �������
        Debug.Log(Vector3.Distance(v, v2));
        // ��� (������ˣ����Ϊ ��� �ֳ� ������ �� ������)����ӳ�����������ڷ����ϵ����ƶȣ�Խ��Խ����
        Vector3.Dot(v, v2);
        // ��� �������������ƽ���ı��Σ�������˽���������ƽ���ı������
        Vector3.Cross(v, v2);
        // ��ֵ
        Vector3.Lerp(v, v2, 0.8f);
        // ������ģ
        Debug.Log(v.magnitude);
        // �淶������
        Debug.Log(v.normalized);
    }

    void Update()
    {
        
    }
}
