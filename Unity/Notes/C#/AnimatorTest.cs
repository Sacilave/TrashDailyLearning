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
            // animator.Play("left");  播放 名为 left 的 State
        }
        if (Input.GetMouseButtonDown(1))
        {
            // animator.Play("right");  播放名为 right 的 State
        }
        if (Input.GetKeyDown(KeyCode.F))
        {
            GetComponent<Animator>().SetTrigger("ifPickUp");  // 设置 ifPickUp 这个 Trigger parameter 为触发状态
        }
    }
}
