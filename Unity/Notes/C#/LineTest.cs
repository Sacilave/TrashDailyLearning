using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LineTest : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        // ����߶�λ��
        LineRenderer lineRenderer = GetComponent<LineRenderer>();
        lineRenderer.positionCount = 3;  // ����Line��ê�����
        lineRenderer.SetPosition(0, Vector3.zero);  // ���õ������λ�� (�� 0 ����λ��)������ʹ�� SetPositions() ���ö�����λ�ã�����Ϊһ�����飬����Ԫ�طֱ��Ӧ�������λ��
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
