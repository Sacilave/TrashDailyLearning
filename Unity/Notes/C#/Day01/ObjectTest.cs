using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class ObjectTest : MonoBehaviour
{
    public GameObject Cube;  // ��ȡһ�� GameObject ���͵� Cube
    public GameObject Prefab;  // ��ȡһ�� Prefab
    void Start()
    {
        // �õ���ǰ�ű����ص���Ϸ����
        // GameObject go = this.gameObject;  �������嶼���� gameObject �࣬this.gameObject ��ʾ����ű�������� gameObject �࣬Ҳ���Բ�ʹ�� this
        Debug.Log(gameObject.name);  // name
        Debug.Log(gameObject.tag);  // tag
        Debug.Log(Cube.layer);  // layer


        // ��ȡ��������״̬(����������丸��δ�����������Ҳ��δ�����)
        Debug.Log(Cube.activeInHierarchy);
        // ��ȡ������״̬
        Debug.Log(Cube.activeSelf);
        // ���ü���״̬
        Cube.SetActive(false);


        // ��ȡ�������� transform ���
        Debug.Log(transform.position);  // ���е� transform Ϊ this.transform
        // ��ȡ����������� (�� BoxCollider)
        BoxCollider bc = GetComponent<BoxCollider>();
        // ��ȡ��ǰ�����������ĳ�����
        GetComponentInChildren<BoxCollider>(bc);
        // ��ȡ��ǰ���常�����ĳ�����
        GetComponentInParent<BoxCollider>();
        // �Լ�������
        gameObject.AddComponent<AudioSource>();
        // ����������������
        Cube.AddComponent<AudioSource>();


        // ͨ����Ϸ�������ƻ�ȡ��Ϸ����
        GameObject findByName = GameObject.Find("Plane");
        // ͨ����Ϸ��ǩ��ȡ����
        GameObject findByTag = GameObject.FindWithTag("Player");


        // ͨ�� Prefab ʵ����һ������
        GameObject go = Instantiate(Prefab, Vector3.zero, Quaternion.identity);  // Instantiate(ʵ����)��ʵ�������ŵ�����0,0,0�ϲ���ת
        // ��������
        Destroy(go);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
