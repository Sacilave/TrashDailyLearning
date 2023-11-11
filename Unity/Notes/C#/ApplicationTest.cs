using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ApplicationTest : MonoBehaviour
{
    // ��Ϸ�ļ���ϵͳ��Ĳ���
    void Start()
    {
        // ��Ϸ��д�ļ�����
        // ��Ϸ�����ļ���·��
        Debug.Log(Application.dataPath);  // ֻ��������ѹ��
        // �־û��ļ�·�� (�������κ�ƽ̨)
        Debug.Log(Application.persistentDataPath);  // ������д���ļ�
        // StreamingAssets �ļ��� 
        Debug.Log(Application.streamingAssetsPath);  // ֻ���������ܣ������������ļ�
        // ��ʱ�ļ���
        Debug.Log(Application.temporaryCachePath);

        // ���Ƴ����Ƿ��̨����
        Debug.Log(Application.runInBackground);
        // �� URL
        Application.OpenURL("www.google.com");
        // �˳���Ϸ
        Application.Quit();

    }

    void Update()
    {
        
    }
}
