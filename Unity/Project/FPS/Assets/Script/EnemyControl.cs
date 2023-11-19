using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.UIElements;

public class EnemyControl : MonoBehaviour
{
    public int HP = 5;
    public Transform player;
    public float stopDistance = 2.0f;  // ×î½ü¾àÀë
    public float speed = 3.0f;
    public Text score;
    public GameObject enemy;
    private Animator animator;


    void Start()
    {
        animator = GetComponent<Animator>();
        animator.SetBool("EnemyWalk", true);
        
    }

    void Update()
    {
        if (Vector3.Distance(transform.position, player.position) > stopDistance)
        {
            animator.SetBool("EnemyWalk", true);
            transform.position = Vector3.MoveTowards(transform.position, player.position, speed * Time.deltaTime);
        }
        else animator.SetBool("EnemyWalk", false);

    }
    private void OnTriggerEnter(Collider other)
    {
        if (other.tag == "Bullet")
        {
            HP--;
            if (HP < 0) 
            {
                Destroy(gameObject);
                score.text = int.Parse(score.text) + 10 + "";
            }
            
        }
    }
}
