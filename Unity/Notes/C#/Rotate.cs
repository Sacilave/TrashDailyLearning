using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotate : MonoBehaviour
{
    void Start()
    {
        // ��ת��ʹ�� ŷ���� �� ��Ԫ��
        Vector3 rotateEuler = new Vector3(0, 30, 0);  // �½�һ�� y�� ��ת30�ȵ���ά�������
        Quaternion rotateQuaternion = Quaternion.identity;  // �½�һ�� ��Ԫ������ 
        // ŷ����תΪ��Ԫ��
        rotateQuaternion = Quaternion.Euler(rotateEuler);
        // ��Ԫ��ת��Ϊŷ����
        rotateEuler = rotateQuaternion.eulerAngles;
        // ����һ����������ת
        rotateQuaternion = Quaternion.LookRotation(new Vector3(0, 0, 0));  // �������½���һ����ά����
    }

    void Update()
    {
        
    }
}
