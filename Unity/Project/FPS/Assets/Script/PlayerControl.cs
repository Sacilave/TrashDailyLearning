using System.Collections;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using UnityEngine;
using UnityEngine.UI;

public class PlayerControl : MonoBehaviour
{
    public float jumpForce = 200;
    public Text healthText;

    private Rigidbody rb;  // ¸ÕÌå
    private AudioSource footstepPlayer;  // ÒôÆµ×é¼þ
    private bool isGround;
    private int health = 100;
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        footstepPlayer = GetComponent<AudioSource>();

    }
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space) && isGround)  // ÌøÔ¾
        {
            rb.AddForce(Vector3.up * jumpForce);
        }

        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");
        if ((horizontal != 0 || vertical != 0) && isGround)
        {
            if (!footstepPlayer.isPlaying)
            {
                footstepPlayer.Play();
            }
        }
        else
        {
            footstepPlayer.Stop();
        }
    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.collider.tag == "Ground")
        {
            isGround = true;
        }
        if (collision.collider.tag == "Enemy")
        {
            Invoke("healthDecrease", 1);
            healthText.text = health + "";
        }
    }
    private void OnCollisionExit(Collision collision)
    {
        if (collision.collider.tag == "Ground")
        {
            isGround = false;
        }
    }
    void healthDecrease()
    {
        health -= 10;
    }
}
