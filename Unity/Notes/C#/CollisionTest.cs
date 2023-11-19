using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CollisionTest : MonoBehaviour
{
    public GameObject Prefab;  // 假设此处获取了一个爆炸效果，此脚本放在了一个炸弹的 prefab 上
    void Start()
    {
        
    }

    void Update()
    {
        
    }
    private void OnCollisionEnter(Collision collision)  // 监听发生碰撞，参数中的 Collision 为碰撞到的物体
    {
        Instantiate(Prefab, transform.position, Quaternion.identity);  // 将 Prefab 生成为一个物体，也就是让爆炸效果生成
        Destroy(gameObject);  // 销毁生成出的炸弹物体
        // 但是此时爆炸效果这个物体没被销毁
        // 重点：需要新建一个 C#对象 给爆炸效果这个 prefab，设置timer，定时几秒并销毁。此时若 爆炸效果prefab 被 Instantiate，timer启动后自动将自身销毁
        // 重要思想：物体自身行为 使用 自身C#对象实现

        Debug.Log(collision.gameObject.name);
    }
    private void OnCollisionStay(Collision collision)  // 持续碰撞中
    {
        
    }
    private void OnCollisionExit(Collision collision)  // 碰撞结束
    {
        
    }
}
