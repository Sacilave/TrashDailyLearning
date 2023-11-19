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
        float horizontal = Input.GetAxis("Horizontal");  // ˮƽ�� AD
        float vertical = Input.GetAxis("Vertical");  // ��ֱ�� WS

        Vector3 dir = new Vector3(horizontal, 0, vertical);  // ����һ����������
        // Debug.DrawRay(transform.position, dir, Color.red);
        player.SimpleMove(dir * 2);  // ����÷����ƶ���Move() ��������Ӱ�죬SimpleMove() ������Ӱ�죬����Ϊ����
    }
}
