using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ApplicationTest : MonoBehaviour
{
    // 游戏文件与系统间的操作
    void Start()
    {
        // 游戏读写文件操作
        // 游戏数据文件夹路径
        Debug.Log(Application.dataPath);  // 只读，加密压缩
        // 持久化文件路径 (适用于任何平台)
        Debug.Log(Application.persistentDataPath);  // 常用于写入文件
        // StreamingAssets 文件夹 
        Debug.Log(Application.streamingAssetsPath);  // 只读，不加密，常用于配置文件
        // 临时文件夹
        Debug.Log(Application.temporaryCachePath);

        // 控制程序是否后台运行
        Debug.Log(Application.runInBackground);
        // 打开 URL
        Application.OpenURL("www.google.com");
        // 退出游戏
        Application.Quit();

    }

    void Update()
    {
        
    }
}
