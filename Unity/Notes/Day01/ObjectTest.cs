using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class ObjectTest : MonoBehaviour
{
    public GameObject Cube;  // 获取一个 GameObject 类型的 Cube
    public GameObject Prefab;  // 获取一个 Prefab
    void Start()
    {
        // 拿到当前脚本挂载的游戏物体
        // GameObject go = this.gameObject;  所有物体都属于 gameObject 类，this.gameObject 表示这个脚本的物体的 gameObject 类，也可以不使用 this
        Debug.Log(gameObject.name);  // name
        Debug.Log(gameObject.tag);  // tag
        Debug.Log(Cube.layer);  // layer


        // 获取真正激活状态(比如自身激活但其父级未激活导致其自身也是未激活的)
        Debug.Log(Cube.activeInHierarchy);
        // 获取自身激活状态
        Debug.Log(Cube.activeSelf);
        // 设置激活状态
        Cube.SetActive(false);


        // 获取物体自身 transform 组件
        Debug.Log(transform.position);  // 其中的 transform 为 this.transform
        // 获取其他物体组件 (如 BoxCollider)
        BoxCollider bc = GetComponent<BoxCollider>();
        // 获取当前物体子物体的某个组件
        GetComponentInChildren<BoxCollider>(bc);
        // 获取当前物体父物体的某个组件
        GetComponentInParent<BoxCollider>();
        // 自己添加组件
        gameObject.AddComponent<AudioSource>();
        // 给其他物体添加组件
        Cube.AddComponent<AudioSource>();


        // 通过游戏物体名称获取游戏物体
        GameObject findByName = GameObject.Find("Plane");
        // 通过游戏标签获取物体
        GameObject findByTag = GameObject.FindWithTag("Player");


        // 通过 Prefab 实例化一个物体
        GameObject go = Instantiate(Prefab, Vector3.zero, Quaternion.identity);  // Instantiate(实例化)，实例化并放到世界0,0,0上不旋转
        // 销毁物体
        Destroy(go);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
