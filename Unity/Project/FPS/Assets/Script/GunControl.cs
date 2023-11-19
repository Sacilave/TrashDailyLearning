using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GunControl : MonoBehaviour
{
    public Transform FirePoint;
    public GameObject FirePre;
    public Transform BulletPoint;
    public GameObject BulletPre;
    public AudioClip clip;  // �����ӵ���Ч
    public AudioClip check;  // ����������Ч
    public Text BulletText;  // �����ӵ�UI

    private int bulletCount = 20;  // �����ӵ���
    private float cd = 0.2f;  // ������ʱ��
    private float timer = 0;  // ��ʱ��
    private AudioSource gunPlayer;  // �����������
    void Start()
    {
        gunPlayer = GetComponent<AudioSource>();
        BulletText.text = bulletCount.ToString();
    }

    // Update is called once per frame
    void Update()
    {
        timer += Time.deltaTime;  // ��ʱ
        if (timer > cd && Input.GetMouseButton(0) && bulletCount > 0)  // GetMouseButton �� 0 Ϊ�����1 Ϊ�Ҽ�
        {
            timer = 0;  // ���ü�ʱ��
            Instantiate(FirePre, FirePoint.position, FirePoint.rotation);  // ��������
            Instantiate(BulletPre, BulletPoint.position, BulletPoint.rotation);  // �����ӵ�
            bulletCount --;
            BulletText.text = bulletCount.ToString();  // ˢ���ӵ��� UI
            gunPlayer.PlayOneShot(clip);
            if (bulletCount == 0)
            {
                GetComponent<Animator>().SetTrigger("Reload");
                gunPlayer.PlayOneShot(check);
                Invoke("Reload", 1.5f);  // �ӳ� 1.5s ����� Reload ����
            }
        }

        // �ֶ�����
        if (Input.GetKeyDown(KeyCode.R))
        {
            bulletCount = 0;
            GetComponent<Animator>().SetTrigger("Reload");
            gunPlayer.PlayOneShot(check);
            Invoke("Reload", 1.5f);  // �ӳ� 1.5s ����� Reload ����
        }

    }

    void Reload()
    {
        bulletCount = 20;
        BulletText.text = bulletCount.ToString();
    }
}
