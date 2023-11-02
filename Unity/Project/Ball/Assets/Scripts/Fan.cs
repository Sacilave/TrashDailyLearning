using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Fan : MonoBehaviour
{
    bool isInRange;
    public Rigidbody rb;
    public float fanPower;
    Vector3 input;

    private void Start()
    {
        isInRange = false;
    }

    void Update()
    {
        float h = Input.GetAxis("Horizontal");
        input = new Vector3(h, 0, 0).normalized;
        if (isInRange)
        {
            rb.velocity -= input*fanPower;
        }
    }
    private void OnTriggerEnter(Collider other)
    {
        if (other.tag == "Player") isInRange = true;
        
    }
}
