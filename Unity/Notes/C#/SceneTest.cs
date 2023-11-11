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


        Debug.Log(SceneManager.sceneCount);  // ��ȡ�Ѽ��صĳ������� 
        Scene newScene = SceneManager.CreateScene("newScene");  // �����³���
        SceneManager.UnloadSceneAsync(newScene);  // ж�س���
        // ���س���  LoadScene(��������, ���ط�ʽ)
        SceneManager.LoadScene("MyScene", LoadSceneMode.Single);  // Single Ϊ �滻������Additive Ϊ ��ӳ��� (ԭ�������ᱻ�ر�)

    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
