#include <stdio.h>
#include <stdbool.h>
#include <Windows.h>
#include <stdlib.h>

// Circle C, S
void d6Circle() {
	const float PI = 3.1415; int r;
	printf("请输入圆的半径：\n");
	scanf("%d", &r);
	printf("圆的周长为：%.2f, 面积为 %.2f\n", 2 * PI * r, PI * r * r);
}

// Output the input type
void d6InputType() {
	char input; int numInput;
	printf("请输入字符：\n");
	scanf("%c", &input);
	numInput = (int)input;
	if (numInput >= 48 && numInput <= 57) printf("输入为数字\n");
	else if (numInput >= 65 && numInput <= 90) printf("输入为大写字母\n");
	else if (numInput >= 97 && numInput <= 122) printf("输入为小写字母\n");
	else if (numInput == 32) printf("输入为空格\n");
	else printf("输入为其他字符\n");
}

// 回文数
void d6NumTest() {
	int num[5]; bool flag = true; int input;
	printf("输入一串数字：\n");
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
	if (flag) printf("是回文数\n");
	else printf("不是回文数\n");
}

// 自动提款机

void d6Call();

void ifRecall() {
	char flag = false;
	scanf("%c", &flag);
	printf("是否进行重新输入（y / n）\n");
	scanf("%c", &flag);
	if (flag == 'y') d6Call();
	else return;
}

void d6Call() {
	char input;
	printf("请输入1-4的数字，选择完成的功能：");
	scanf("%c", &input);
	switch (input)
	{
	default:
		printf("输入错误，重新输入\n");
		d6Call();
		break;
	case '1':
		printf("选择了查询功能\n");
		ifRecall();
		break;
	case '2':
		printf("选择了存款功能\n");
		ifRecall();
		break;
	case '3':
		printf("选择了取款功能\n");
		ifRecall();
		break;
	case '4':
		printf("选择了转账功能\n");
		ifRecall();
		break;
	}
}

void d6BankMenu() {
	printf("*******\n自助提款机\n1.查询\n2.存款\n3.取款\n4.转账\n*******\n");
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
				if (i * 3 + j * 2 + h == 50 && i + j + h == 30) { printf("男人 %d, 女人 %d, 小孩 %d\n", i, j, h); count++; }
			}
		}
	}
	printf("一共 %d 中可能\n", count);
}

void d6Callatz() {
	int n, count = 0;
	printf("输入一个数：\n");
	scanf("%d", &n);
	while (n > 0) {
		if (n == 1) break;
		else if (n % 2 == 0) n /= 2;
		else n = (3 * n + 1) / 2;
		count++;
	}
	printf("需要 %d 步\n", count);
}

void d6ArrTest() {
	int count, arrResCount = 0;
	scanf("%d\n", &count);
	int* arr = (int*)malloc(count * sizeof(int));
	int* arrRes = (int*)malloc(count * sizeof(int));
	for (int i = 0; i < count; i++)  // 获取
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