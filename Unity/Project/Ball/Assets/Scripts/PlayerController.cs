using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class PlayerController : MonoBehaviour
{
    public Rigidbody rb;
    public float moveForce;
    public int nextStageIndex;
    Vector3 input;
    Vector3 startPosition;

    void Start()
    {
        startPosition = transform.position;
    }

    void Update()
    {
        float h = Input.GetAxis("Horizontal");
        float v = Input.GetAxis("Vertical");

        input = new Vector3 (h, 0, v).normalized;

    }

    private void FixedUpdate()
    {
        rb.AddForce(input * moveForce);
    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.tag == "Wall") transform.position = startPosition;

    }
    private void OnTriggerEnter(Collider other)
    {
        if (other.tag == "Goal") SceneManager.LoadScene(nextStageIndex);
    }
}
