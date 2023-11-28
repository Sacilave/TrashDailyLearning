using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimatorTest : MonoBehaviour
{
    private Animator animator;
    public Transform target;
    public int Speed = 3;

    void Start()
    {
        animator = GetComponent<Animator>();
        animator.Play("pickup");  // 播放名为 pickup 的 State
    }

    // Update is called once per frame
    void Update()
    {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");
        Vector3 dir = new Vector3(horizontal, 0, vertical);  // 声明方向向量
        if (Input.GetKey(KeyCode.LeftShift))
        {
            animator.SetBool("IsRun", true);  // 设置名为 IsRun 的 Bool 为 true
            Speed = 6;
        }
        else
        {
            animator.SetBool("IsRun", false);
            Speed = 3;
        }
        if (dir != Vector3.zero)
        {
            transform.rotation = Quaternion.LookRotation(dir);  // 让角色面向向量，方向与方向向量相同 (四元数类型)
            animator.SetBool("IsWalk", true);
            transform.Translate(Vector3.forward * Speed * Time.deltaTime);  // 向前移动 2 米
        }
        else animator.SetBool("IsWalk", false);
        if (Input.GetKeyDown(KeyCode.F)) animator.SetTrigger("ifPickUp");  // 设置名为 ifPickUp 的 Trigger 为激活状态

        Debug.Log(animator.GetFloat("TestCurve"));   // 获取名为 TestCurve 的参数值，同时也有 GetBool() 等等方法用于获取

    }

    void rightFoot()  // 此函数为 Events 中设置触发的 event
    {
        Debug.Log("右脚");
    }
    void leftFoot()  // 同上
    {
        Debug.Log("左脚");
    }
    private void OnAnimatorIK(int layerIndex)  // 所有IK相关的脚本都写在此方法中
    {
        // 设置头部IK
        animator.SetLookAtWeight(1);  // 设置权重，0~1
        animator.SetLookAtPosition(target.position);  // 设置看向位置 

        // 设置右手IK
        animator.SetIKPositionWeight(AvatarIKGoal.RightHand, 1);  // 设置位置受IK影响权重
        animator.SetIKRotationWeight(AvatarIKGoal.RightHand, 1);  // 设置旋转受IK影响权重
        animator.SetIKPosition(AvatarIKGoal.RightHand, target.position);  // 设置位置
        animator.SetIKRotation(AvatarIKGoal.RightHand, target.rotation);  // 设置旋转
    }
}
