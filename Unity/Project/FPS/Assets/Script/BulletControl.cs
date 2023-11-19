using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BulletControl : MonoBehaviour
{
    public int BulletSpeed = 1000;
    void Start()
    {
        GetComponent<Rigidbody>().AddForce(transform.forward * BulletSpeed);
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.name != "MapCollider") Destroy(gameObject);
    }
    private void OnTriggerExit(Collider other)
    {
        if (other.name == "MapCollider") Destroy(gameObject);
    }
}
