#include <stdio.h>
#include <Math.h>

// 金字塔
int piramid() {
    char input; int c;
    printf("金字塔字符 和 金字塔层数：\t");
    scanf("%c%d", &input, &c);
    for (int i = 1; i < c+1; i++) {
        for (int j = 0; j < c - i; j++)
        {
            printf(" ");
        }
        for (int j = 0; j < 2 * i-1; j++)
        {
            printf("%c", input);
        }
        printf("\n");
    }
}

// 字母转换
int letterTrans() {
    int inputNum;
    printf("输入字母：\n");
    scanf("%c", &inputNum);
    printf("大写字母为：%c\n", inputNum - 32);
}

// 数字反转 (如输入 123.4 , 输出 432.1)
int numTurn() {
    int forward, backward; float output = 0.0;
    scanf("%d.%d", &forward, &backward);
    output += backward;
    for (int i = 1; i < 4; i++)
    {
        output += ((forward % 10 )* pow(0.1, i));
        forward /= 10;
    }
    printf("%.3f", output);
}

// P5706 【深基2.例8】再分肥宅水
int a() {
    float t; int n;
    scanf("%f %d", &t, &n);
    printf("%.3f\n%d", t / n, 2 * n);
}

// P5708 【深基2.习2】三角形面积
int b() {
    float a, b, c, p;
    scanf("%f %f %f", &a, &b, &c);
    p = (a + b + c) / 2;
    printf("%.1f", sqrt(p * (p - a) * (p - b) * (p - c)));
}

// P5707 【深基2.例12】上学迟到
int c() {
    int s, v, t, temp;
    int hour, minute;
    scanf("%d %d", &s, &v);

    if (s % v == 0) { t = s / v + 10; }
    else { t = s / v + 11; }

    if (t <= 480)
    {
        temp = 480 - t;
        hour = temp / 60;
        minute = temp % 60;
    }

    else
    {
        hour = 0;
        minute = 0;
    }
    printf("%02d:%02d", hour, minute);
}

int main() {
    c();
}