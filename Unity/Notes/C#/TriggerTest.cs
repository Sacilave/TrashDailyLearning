using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TriggerTest : MonoBehaviour
{
    public GameObject player;
    // 将物体设置为 isTrigger，与 collision 相同，只是从检测碰撞变成了检测
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
