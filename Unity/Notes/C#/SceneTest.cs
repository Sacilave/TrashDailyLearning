using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneTest : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        SceneManager.LoadScene(0);  // 场景跳转，可以使用 场景索引 和 场景名称
        Scene scene = SceneManager.GetActiveScene();  // 获取当前的场景
        Debug.Log(scene.name);  // 场景名称
        /*
        scene.isLoaded  是否被加载
        scene.path  场景路径
        scene.buildIndex  场景索引
        */
        GameObject[] gos = scene.GetRootGameObjects();  // 获取场景内所有游戏物体，返回数组


        Debug.Log(SceneManager.sceneCount);  // 获取已加载的场景数量 
        Scene newScene = SceneManager.CreateScene("newScene");  // 创建新场景
        SceneManager.UnloadSceneAsync(newScene);  // 卸载场景
        // 加载场景  LoadScene(场景名称, 加载方式)
        SceneManager.LoadScene("MyScene", LoadSceneMode.Single);  // Single 为 替换场景，Additive 为 添加场景 (原场景不会被关闭)

    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
