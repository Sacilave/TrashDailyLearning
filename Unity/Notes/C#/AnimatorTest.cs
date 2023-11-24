using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimatorTest : MonoBehaviour
{
    private Animator animator;
    public int Speed = 3;
    void Start()
    {
        animator = GetComponent<Animator>();
        animator.Play("pickup");  // ������Ϊ pickup �� State
    }

    // Update is called once per frame
    void Update()
    {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");
        Vector3 dir = new Vector3(horizontal, 0, vertical);  // ������������
        if (Input.GetKey(KeyCode.LeftShift))
        {
            animator.SetBool("IsRun", true);  // ������Ϊ IsRun �� Bool Ϊ true
            Speed = 6;
        }
        else
        {
            animator.SetBool("IsRun", false);
            Speed = 3;
        }
        if (dir != Vector3.zero)
        {
            transform.rotation = Quaternion.LookRotation(dir);  // �ý�ɫ���������������뷽��������ͬ (��Ԫ������)
            animator.SetBool("IsWalk", true);
            transform.Translate(Vector3.forward * Speed * Time.deltaTime);  // ��ǰ�ƶ� 2 ��
        }
        else animator.SetBool("IsWalk", false);
        if (Input.GetKeyDown(KeyCode.F)) animator.SetTrigger("ifPickUp");  // ������Ϊ ifPickUp �� Trigger Ϊ����״̬

        Debug.Log(animator.GetFloat("TestCurve"));   // ��ȡ��Ϊ TestCurve �Ĳ���ֵ��ͬʱҲ�� GetBool() �ȵȷ������ڻ�ȡ

    }

    void rightFoot()  // �˺���Ϊ Events �����ô����� event
    {
        Debug.Log("�ҽ�");
    }
    void leftFoot()  // ͬ��
    {
        Debug.Log("���");
    }
}
