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
        // VideoPlayer��� �ĳ�Ա������ Play(), Pause() �� AudioPlayer��� ��ͬ
    }
}
