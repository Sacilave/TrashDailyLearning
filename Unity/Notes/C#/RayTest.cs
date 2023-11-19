using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// ��ʵ�������ϵ��ӽǵ�RPG�У��������ɫ��������Ĺ���

public class RayTest : MonoBehaviour
{
    void Start()
    {
        // ��������
        Ray ray01 = new Ray(Vector3.zero, Vector3.up);  // ��ʽһ���� (0,0,0) �㴴����һ�����ϵ�����
        ray01 = Camera.main.ScreenPointToRay(Input.mousePosition);  // ��ʽ����ͨ�� main Camera �����һ������
    }

    void Update()
    {
        if (Input.GetMouseButtonDown(0))  
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);  // ��������
            RaycastHit hit;  // ������ײ��Ϣ��
            bool res = Physics.Raycast(ray, out hit);  // ��ײ��� �� out �������ͣ�������ֵ��ֵ������� hit ����������Ҳ���Ǿ�������㣩
            
            if (res)
            {
                Debug.Log(hit.point);
                transform.position = hit.point;  // ���� position Ϊ ��ȡ��ײ�� position
            }

            // ���⣺RaycastHit[] hits = Physics.RaycastAll(ray, 100, 1<<10); (���ߣ������룬���ͼ��(����Ϊͼ�� 10))
        }
    }
}
