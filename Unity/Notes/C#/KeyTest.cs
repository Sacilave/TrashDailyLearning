using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class KeyTest : MonoBehaviour
{
    void Start()
    {
        
    }

    void Update()
    {
        // ���ĵ��
        // ������� 0���  1�Ҽ�  2����
        if (Input.GetMouseButtonDown(0)) { }
        // �����������
        if (Input.GetMouseButton(0)) { }
        // ̧�����
        if (Input.GetMouseButtonUp(0)) { }

        // ���̰���
        // ���¼��̰���
        if (Input.GetKeyDown(KeyCode.Space));  // KeyCode Ϊö�����ͣ�Ҳ��ʹ���ַ����� "a"�������ִ�Сд
        // �������¼���
        Input.GetKey(KeyCode.K);
        // �ɿ����̰���
        Input.GetKeyUp(KeyCode.Space);
    }
}
