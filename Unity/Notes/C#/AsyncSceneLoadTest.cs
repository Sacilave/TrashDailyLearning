using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class AsyncSceneLoadTest : MonoBehaviour
{
    AsyncOperation operation;
    void Start()
    {
        StartCoroutine(loadScene());  // 开始协程
    }
    
    // 协程方法来异步加载场景 (用于大场景加载)
    IEnumerator loadScene()
    {
        operation = SceneManager.LoadSceneAsync(1);
        operation.allowSceneActivation = false;  // 加载完场景不要自动跳转，如需跳转了直接设置为 true 就行 (可以实现按任意键跳转场景)
        yield return operation;
    }

    // Update is called once per frame
    void Update()
    {
        Debug.Log(operation.progress);  // 输出加载进度 0 ~ 0.9
    }
}
