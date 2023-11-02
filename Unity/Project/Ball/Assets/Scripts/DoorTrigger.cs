using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DoorTrigger : MonoBehaviour
{
    public GameObject Door;
    bool isActive;
    void Update()
    {
        if (isActive && Door.transform.position.y > -3.57f) Door.transform.position -= new Vector3(0, 0.5f * Time.deltaTime, 0);
    }
    private void OnTriggerEnter(Collider other)
    {
        if (other.tag == "Player") isActive = true;
    }
}
