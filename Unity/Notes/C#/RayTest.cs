using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// 可实现类似上帝视角的RPG中，点哪里角色走向哪里的功能

public class RayTest : MonoBehaviour
{
    void Start()
    {
        // 创建射线
        Ray ray01 = new Ray(Vector3.zero, Vector3.up);  // 方式一，在 (0,0,0) 点创建了一个向上的射线
        ray01 = Camera.main.ScreenPointToRay(Input.mousePosition);  // 方式二，通过 main Camera 发射出一个射线
    }

    void Update()
    {
        if (Input.GetMouseButtonDown(0))  
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);  // 发射射线
            RaycastHit hit;  // 声明碰撞信息类
            bool res = Physics.Raycast(ray, out hit);  // 碰撞检测 （ out 传参类型，将返回值赋值给传入的 hit 变量参数，也就是具体坐标点）
            
            if (res)
            {
                Debug.Log(hit.point);
                transform.position = hit.point;  // 设置 position 为 获取碰撞点 position
            }

            // 多检测：RaycastHit[] hits = Physics.RaycastAll(ray, 100, 1<<10); (射线，检测距离，检测图层(例如为图层 10))
        }
    }
}
