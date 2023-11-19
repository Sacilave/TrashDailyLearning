using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerControl : MonoBehaviour
{
    private CharacterController player;
    void Start()
    {
        player = GetComponent<CharacterController>();
    }

    void Update()
    {
        float horizontal = Input.GetAxis("Horizontal");  // 水平轴 AD
        float vertical = Input.GetAxis("Vertical");  // 垂直轴 WS

        Vector3 dir = new Vector3(horizontal, 0, vertical);  // 创建一个方向向量
        // Debug.DrawRay(transform.position, dir, Color.red);
        player.SimpleMove(dir * 2);  // 朝向该方向移动，Move() 不受重力影响，SimpleMove() 受重力影响，参数为方向
    }
}
