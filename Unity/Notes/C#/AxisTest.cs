using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AxisTest : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        float horizontal = Input.GetAxis("Horizontal");
        Input.GetButtonDown("Jump");  // ͬʱҲ���� GetButton, GetButtonUp �������� Project Settings��Input Manager ���и�������������ⰴ���Ķ���
    }
}
