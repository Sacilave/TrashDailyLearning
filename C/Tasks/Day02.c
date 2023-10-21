#include <stdio.h>
#include <stdbool.h>
#include <math.h>

// �ж���ż��
void oddEven() {
	int inputNum = 0;
	printf("��������\n");
	if (scanf("%d", &inputNum) % 2 == 0) printf("��ż��\n");
	else printf("������\n");
}

// �ж�����������
bool judgeRT(float a, float b, float c) {
	return pow(a, 2) + pow(b, 2) == pow(c, 2);
}
void triangle() {
	float a, b, c = 1;
	while (1)
	{
		printf("�������������߳���,�ָ�\n");
		scanf("%f,%f,%f", &a, &b, &c);
		if ((a + b <= c) || (a + c <= b) || (b + c <= a)) {
			printf("������������, ��������\n");
			continue;
		}
		else
		{
			if (judgeRT(a, b, c) || judgeRT(a, c, b) || judgeRT(b, c, a)) printf("��ֱ��������\n");
			if (a == b && a ==c && b ==c) printf("�ǵȱ�������\n");
			else if (a == b || a == c || b == c) printf("�ǵ���������\n");
			break;
		}
	}
}

// �ж�ʣ������
void oilWatcher() {
	float oil = 0;
	printf("ʣ������\n");
	scanf("%f", &oil);
	if (oil < 0.25) printf("�����ͣ�ע�⣡\n");
	else if (oil >= 3.0 / 4.0) printf("������������ͣ��\n");
}

// ���Сʱ�ͷ���
void hourMin() {
	int hour, min = 0;
	printf("����Сʱ�ͷ�����,�ָ�\n");
	scanf("%d,%d", &hour, &min);
	printf("%02d:%02d", hour, min);
}

// ����������
void calculator() {
	char calcu = '+'; int a = 0, b = 0;
	printf("������ʽ\n");
	scanf("%d%c%d", &a, &calcu, &b);
	switch (calcu) {
		default: printf("�����������"); break;
		case '+': printf("%d%c%d=%d", a, calcu, b, a + b); break;
		case '-': printf("%d%c%d=%d", a, calcu, b, a - b); break;
		case '*': printf("%d%c%d=%d", a, calcu, b, a * b); break;
		case '/': printf("%d%c%d=%d", a, calcu, b, a / b); break;
	}
}

// �����ּ�
void scoreSeperate() {
	int score = 0;
	printf("�������\n");
	scanf("%d", &score);
	switch (score / 10) {
		default: printf("������\n"); break;
		case 6: printf("����\n"); break;
		case 7: printf("�е�\n"); break;
		case 8: printf("����\n"); break;
		case 9: case 10: printf("����\n"); break;
	}
}

// ���ĳ���м���
void monthOutput() {
	int year = 0, month = 0, runMonth = 28;
	printf("������ݺ��·�\n");
	scanf("%d %d", &year, &month);
	if (year % 4 == 0 && year % 100 != 0) runMonth = 29;
	switch (month) { 
		default: printf("����30��"); break;
		case 1: case 3: case 5: case 7: case 8: case 10: case 12: printf("����31��"); break;
		case 2:printf("����%d��", runMonth); break;
	}
}