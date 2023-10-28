using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LifeCycle : MonoBehaviour
{
    /* �ű�����������
    Awake()  ������ã�����ʹ�õ���ģʽ
    OnEnable()  �����������һ�Σ�Awake() ���ú��Զ�����һ�Σ�������ֵ�ĳ�ʼ��
    Start()  �� Update ֮ǰ����һ�Σ������������ó�ʼֵ
    FixedUpdate()  �̶�Ƶ�ʵ��ã�ʱ������ͬ��Ĭ��0.02s������ U3d ���޸ģ�Edit, Project Settings, Time, Fixed Timestep ���޸�
    Update()  ÿ֡����һ��
    LateUpdate()  ÿ�� Update() ������󱻵���
    OnDisable()  ���δ����ʱ����
    OnDestroy()  ��������ٺ����һ��
     */

    void Awake()
    {
        Debug.Log("Awake function enabled");  // ���
    }
    void Start()
    {
        
    }
    void Update()
    {
        
    }
    void FixedUpdate()
    {
        // Debug.Log("FixedUpdate() enabled, frequency 0.02s");
    }
}
