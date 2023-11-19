using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Video;

public class VideoTest : MonoBehaviour
{
    private VideoPlayer player;
    void Start()
    {
        player = GetComponent<VideoPlayer>();
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space)) player.Play();
        // VideoPlayer组件 的成员函数如 Play(), Pause() 与 AudioPlayer组件 相同
    }
}
