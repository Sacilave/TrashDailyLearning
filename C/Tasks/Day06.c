#include <stdio.h>
#include <stdbool.h>
#include <Windows.h>
#include <stdlib.h>

// Circle C, S
void d6Circle() {
	const float PI = 3.1415; int r;
	printf("������Բ�İ뾶��\n");
	scanf("%d", &r);
	printf("Բ���ܳ�Ϊ��%.2f, ���Ϊ %.2f\n", 2 * PI * r, PI * r * r);
}

// Output the input type
void d6InputType() {
	char input; int numInput;
	printf("�������ַ���\n");
	scanf("%c", &input);
	numInput = (int)input;
	if (numInput >= 48 && numInput <= 57) printf("����Ϊ����\n");
	else if (numInput >= 65 && numInput <= 90) printf("����Ϊ��д��ĸ\n");
	else if (numInput >= 97 && numInput <= 122) printf("����ΪСд��ĸ\n");
	else if (numInput == 32) printf("����Ϊ�ո�\n");
	else printf("����Ϊ�����ַ�\n");
}

// ������
void d6NumTest() {
	int num[5]; bool flag = true; int input;
	printf("����һ�����֣�\n");
	scanf("%d", &input);
	for (int i = 0; i < 5; i++)
	{
		num[i] = input % 10;
		input /= 10;
	}
	for (int i = 0; i < 5; i++)
	{
		printf("%d, %d\n", num[i], num[5 - i - 1]);
		if (num[i] != num[5 - i - 1]) flag = false; 
	}
	if (flag) printf("�ǻ�����\n");
	else printf("���ǻ�����\n");
}

// �Զ�����

void d6Call();

void ifRecall() {
	char flag = false;
	scanf("%c", &flag);
	printf("�Ƿ�����������루y / n��\n");
	scanf("%c", &flag);
	if (flag == 'y') d6Call();
	else return;
}

void d6Call() {
	char input;
	printf("������1-4�����֣�ѡ����ɵĹ��ܣ�");
	scanf("%c", &input);
	switch (input)
	{
	default:
		printf("���������������\n");
		d6Call();
		break;
	case '1':
		printf("ѡ���˲�ѯ����\n");
		ifRecall();
		break;
	case '2':
		printf("ѡ���˴���\n");
		ifRecall();
		break;
	case '3':
		printf("ѡ����ȡ���\n");
		ifRecall();
		break;
	case '4':
		printf("ѡ����ת�˹���\n");
		ifRecall();
		break;
	}
}

void d6BankMenu() {
	printf("*******\n��������\n1.��ѯ\n2.���\n3.ȡ��\n4.ת��\n*******\n");
	d6Call();
}

void d6Coin() {
	int count = 0;
	for (int i = 0; i < 50; i++)
	{
		for (int j = 0; j < 50 - i; j++)
		{
			for (int h = 0; h < 50 - i - j; h++)
			{
				if (i * 3 + j * 2 + h == 50 && i + j + h == 30) { printf("���� %d, Ů�� %d, С�� %d\n", i, j, h); count++; }
			}
		}
	}
	printf("һ�� %d �п���\n", count);
}

void d6Callatz() {
	int n, count = 0;
	printf("����һ������\n");
	scanf("%d", &n);
	while (n > 0) {
		if (n == 1) break;
		else if (n % 2 == 0) n /= 2;
		else n = (3 * n + 1) / 2;
		count++;
	}
	printf("��Ҫ %d ��\n", count);
}

void d6ArrTest() {
	int count, arrResCount = 0;
	scanf("%d\n", &count);
	int* arr = (int*)malloc(count * sizeof(int));
	int* arrRes = (int*)malloc(count * sizeof(int));
	for (int i = 0; i < count; i++)  // ��ȡ
	{
		scanf("%d", &arr[i]);
	}
	for (int i = 0; i < count; i++)
	{
		for (int j = i; j < count; j++) 
		{
			if (arr[i] == arr[j]) {
				arrRes[arrResCount] = arr[i];
				arrResCount++;
			}
		}
	}
	for (int i = 0; i < arrResCount; i++)
	{
		printf("%d\n", arrRes[i]);
	}
}

int main() {
	d6ArrTest();
}