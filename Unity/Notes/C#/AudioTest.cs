using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AudioTest : MonoBehaviour
{
    // AudioClip
    public AudioClip music;
    public AudioClip se;

    // ���������
    private AudioSource player;

    void Start()
    {
        player = gameObject.GetComponent<AudioSource>();
        player.clip = music;  // �趨������Ƶ
        player.loop = true;  // ѭ������
        player.volume = 0.5f;  // ����������float ����
        player.Play();  // ���ţ�һ�����ֻ��ͬʱ����һ������


    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (player.isPlaying)
            {
                player.Pause();  // ��ͣ��Stop Ϊ ֹͣ����
            }
            else player.UnPause();  // ��������
        }
        if (Input.GetMouseButtonDown(0))
        {
            player.PlayOneShot(se);  // ����һ�Σ�������Ч�Ĳ��ţ����ص�����
        }
    }
}
