using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CollisionTest : MonoBehaviour
{
    public GameObject Prefab;  // ����˴���ȡ��һ����ըЧ�����˽ű�������һ��ը���� prefab ��
    void Start()
    {
        
    }

    void Update()
    {
        
    }
    private void OnCollisionEnter(Collision collision)  // ����������ײ�������е� Collision Ϊ��ײ��������
    {
        Instantiate(Prefab, transform.position, Quaternion.identity);  // �� Prefab ����Ϊһ�����壬Ҳ�����ñ�ըЧ������
        Destroy(gameObject);  // �������ɳ���ը������
        // ���Ǵ�ʱ��ըЧ���������û������
        // �ص㣺��Ҫ�½�һ�� C#���� ����ըЧ����� prefab������timer����ʱ���벢���١���ʱ�� ��ըЧ��prefab �� Instantiate��timer�������Զ�����������
        // ��Ҫ˼�룺����������Ϊ ʹ�� ����C#����ʵ��

        Debug.Log(collision.gameObject.name);
    }
    private void OnCollisionStay(Collision collision)  // ������ײ��
    {
        
    }
    private void OnCollisionExit(Collision collision)  // ��ײ����
    {
        
    }
}
