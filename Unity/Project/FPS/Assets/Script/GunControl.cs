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
    public AudioClip clip;  // 关联子弹音效
    public AudioClip check;  // 关联换弹音效
    public Text BulletText;  // 关联子弹UI

    private int bulletCount = 20;  // 弹夹子弹数
    private float cd = 0.2f;  // 开火间隔时间
    private float timer = 0;  // 计时器
    private AudioSource gunPlayer;  // 声音播放组件
    void Start()
    {
        gunPlayer = GetComponent<AudioSource>();
        BulletText.text = bulletCount.ToString();
    }

    // Update is called once per frame
    void Update()
    {
        timer += Time.deltaTime;  // 计时
        if (timer > cd && Input.GetMouseButton(0) && bulletCount > 0)  // GetMouseButton 中 0 为左键，1 为右键
        {
            timer = 0;  // 重置计时器
            Instantiate(FirePre, FirePoint.position, FirePoint.rotation);  // 创建火焰
            Instantiate(BulletPre, BulletPoint.position, BulletPoint.rotation);  // 创建子弹
            bulletCount --;
            BulletText.text = bulletCount.ToString();  // 刷新子弹数 UI
            gunPlayer.PlayOneShot(clip);
            if (bulletCount == 0)
            {
                GetComponent<Animator>().SetTrigger("Reload");
                gunPlayer.PlayOneShot(check);
                Invoke("Reload", 1.5f);  // 延迟 1.5s 后调用 Reload 函数
            }
        }

        // 手动换弹
        if (Input.GetKeyDown(KeyCode.R))
        {
            bulletCount = 0;
            GetComponent<Animator>().SetTrigger("Reload");
            gunPlayer.PlayOneShot(check);
            Invoke("Reload", 1.5f);  // 延迟 1.5s 后调用 Reload 函数
        }

    }

    void Reload()
    {
        bulletCount = 20;
        BulletText.text = bulletCount.ToString();
    }
}
