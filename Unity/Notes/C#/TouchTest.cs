using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TouchTest : MonoBehaviour
{
    void Start()
    {
        Input.multiTouchEnabled = true;  // ������㴥��
    }

    void Update()
    {
        // �жϵ��㴥��
        if (Input.touchCount == 1)  // �жϴ�����Ϊ 1 ��
        {
            // ��������
            Touch touch = Input.touches[0];  // ����Ϊһ���б����ͣ���Ϊ�ǵ��㴥��������ȡ��һ��Ԫ��
            // ����λ��
            Debug.Log(touch.position);
            // �����׶�
            switch (touch.phase)
            {
                case TouchPhase.Began:
                    break;
                case TouchPhase.Moved:
                    break;
                case TouchPhase.Stationary: 
                    break;
                case TouchPhase.Ended:
                    break;
                case TouchPhase.Canceled:
                    break;
            }
        }

        // �ж϶�㴥��
        if (Input.touchCount == 2)  // �жϴ������� 2 ��
        {
            Touch touch = Input.touches[0];
            Touch touch1 = Input.touches[1];  // �м��� �����㣬���м�������Ԫ��
        }
    }
}
