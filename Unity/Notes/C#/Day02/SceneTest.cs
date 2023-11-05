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

        /*
        SceneManager.sceneCount  已加载的场景数量 （可以同时存在多个激活的场景）
         */
        Scene newScene = SceneManager.CreateScene("newScene");
        SceneManager.UnloadSceneAsync(newScene);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
