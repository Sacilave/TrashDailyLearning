#include <stdio.h>
#include <Math.h>

// ������
int piramid() {
    char input; int c;
    printf("�������ַ� �� ������������\t");
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

// ��ĸת��
int letterTrans() {
    int inputNum;
    printf("������ĸ��\n");
    scanf("%c", &inputNum);
    printf("��д��ĸΪ��%c\n", inputNum - 32);
}

// ���ַ�ת (������ 123.4 , ��� 432.1)
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

// P5706 �����2.��8���ٷַ�լˮ
int a() {
    float t; int n;
    scanf("%f %d", &t, &n);
    printf("%.3f\n%d", t / n, 2 * n);
}

// P5708 �����2.ϰ2�����������
int b() {
    float a, b, c, p;
    scanf("%f %f %f", &a, &b, &c);
    p = (a + b + c) / 2;
    printf("%.1f", sqrt(p * (p - a) * (p - b) * (p - c)));
}

// P5707 �����2.��12����ѧ�ٵ�
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