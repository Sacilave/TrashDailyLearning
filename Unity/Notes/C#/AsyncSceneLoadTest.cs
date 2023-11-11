using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class AsyncSceneLoadTest : MonoBehaviour
{
    AsyncOperation operation;
    void Start()
    {
        StartCoroutine(loadScene());  // ��ʼЭ��
    }
    
    // Э�̷������첽���س��� (���ڴ󳡾�����)
    IEnumerator loadScene()
    {
        operation = SceneManager.LoadSceneAsync(1);
        operation.allowSceneActivation = false;  // �����곡����Ҫ�Զ���ת��������ת��ֱ������Ϊ true ���� (����ʵ�ְ��������ת����)
        yield return operation;
    }

    // Update is called once per frame
    void Update()
    {
        Debug.Log(operation.progress);  // ������ؽ��� 0 ~ 0.9
    }
}
