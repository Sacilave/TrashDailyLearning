using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TriggerTest : MonoBehaviour
{
    public GameObject player;
    // ����������Ϊ isTrigger���� collision ��ͬ��ֻ�ǴӼ����ײ����˼��
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private void OnTriggerEnter(Collider other)
    {
        GameObject door = GameObject.Find("Door");
        if (other.gameObject == player && door != null) door.SetActive(false);
    }
}
