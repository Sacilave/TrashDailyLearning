using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneTest : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        SceneManager.LoadScene(0);  // ������ת������ʹ�� �������� �� ��������
        Scene scene = SceneManager.GetActiveScene();  // ��ȡ��ǰ�ĳ���
        Debug.Log(scene.name);  // ��������
        /*
        scene.isLoaded  �Ƿ񱻼���
        scene.path  ����·��
        scene.buildIndex  ��������
        */
        GameObject[] gos = scene.GetRootGameObjects();  // ��ȡ������������Ϸ���壬��������

        /*
        SceneManager.sceneCount  �Ѽ��صĳ������� ������ͬʱ���ڶ������ĳ�����
         */
        Scene newScene = SceneManager.CreateScene("newScene");
        SceneManager.UnloadSceneAsync(newScene);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
