using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TimeTest : MonoBehaviour
{
    float timer = 0;
    void Start()
    {
        // ��Ϸ��ʼ�����ڵ�ʱ��
        Debug.Log(Time.time);
        // ʱ������ֵ
        Debug.Log(Time.timeScale);  // �����ڿ���ʱ��ļ��ټ���
        // �̶�ʱ����
        Debug.Log(Time.fixedDeltaTime);
    }

    void Update()
    {
        // ��һ֡����һ֡���õ�ʱ��
        Debug.Log(Time.deltaTime);  // ������������ʱ��
        timer += Time.deltaTime;
    }
}
