using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AudioTest : MonoBehaviour
{
    // AudioClip
    public AudioClip music;
    public AudioClip se;

    // 播放器组件
    private AudioSource player;

    void Start()
    {
        player = gameObject.GetComponent<AudioSource>();
        player.clip = music;  // 设定播放音频
        player.loop = true;  // 循环播放
        player.volume = 0.5f;  // 设置音量，float 类型
        player.Play();  // 播放，一个组件只能同时播放一个音乐


    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (player.isPlaying)
            {
                player.Pause();  // 暂停，Stop 为 停止播放
            }
            else player.UnPause();  // 继续播放
        }
        if (Input.GetMouseButtonDown(0))
        {
            player.PlayOneShot(se);  // 播放一次，常用音效的播放，可重叠播放
        }
    }
}
