using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TransformTest : MonoBehaviour
{
    void Start()
    {
        // ���λ�� (��Ϊ Vector3 ����)
        Debug.Log(transform.position);  // ����������
        Debug.Log(transform.localPosition);  // local ������ڸ��������

        // ��ȡ��ת (��Ԫ������)
        Debug.Log(transform.rotation);
        Debug.Log(transform.localRotation);
        // ��ȡ��ת (ŷ�������ͣ�Ҳ���� Vector3)
        Debug.Log(transform.eulerAngles);
        Debug.Log(transform.localEulerAngles);

        // ��ȡ����
        Debug.Log(transform.localScale);

        // ��ȡ��������
        Debug.Log(transform.forward);  // x ��
        Debug.Log(transform.right);  // z ��
        Debug.Log(transform.up);  // y ��


        // ���ӹ�ϵ
        GameObject go01 = transform.parent.gameObject;  // ��ȡ������
        int childNum = transform.childCount;  // ���������
        transform.DetachChildren();  // �������������ϵ��
        Transform trans = transform.Find("Child");  // ��ȡ������ͨ������
        Transform trans02 = transform.GetChild(0);  // ��ȡ������ͨ������
        bool res = trans.IsChildOf(transform);  // �ж�һ�������ǲ�����һ�������������
        trans.SetParent(transform);  // �� trans ����Ϊ ������ĸ�����
    }

    void Update()
    {
        transform.LookAt(Vector3.zero);  // ����һ����
        transform.Rotate(Vector3.up, 1);  // ��ת 1��
        transform.RotateAround(Vector3.zero, Vector3.up, 5);  // (�Ƶĵ㣬�Ƶ��ᣬ��ת�ٶ�)
        transform.Translate(Vector3.forward * 0.1f);  // �ƶ�
    }
}
