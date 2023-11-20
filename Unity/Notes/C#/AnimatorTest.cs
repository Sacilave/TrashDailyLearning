using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimatorTest : MonoBehaviour
{
    private Animator animator;
    void Start()
    {
        animator = GetComponent<Animator>();    
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            // animator.Play("left");  ���� ��Ϊ left �� State
        }
        if (Input.GetMouseButtonDown(1))
        {
            // animator.Play("right");  ������Ϊ right �� State
        }
        if (Input.GetKeyDown(KeyCode.F))
        {
            GetComponent<Animator>().SetTrigger("ifPickUp");  // ���� ifPickUp ��� Trigger parameter Ϊ����״̬
        }
    }
}
