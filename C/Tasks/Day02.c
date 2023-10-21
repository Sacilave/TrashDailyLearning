#include <stdio.h>
#include <stdbool.h>
#include <math.h>

// 判断奇偶数
void oddEven() {
	int inputNum = 0;
	printf("输入数字\n");
	if (scanf("%d", &inputNum) % 2 == 0) printf("是偶数\n");
	else printf("是奇数\n");
}

// 判断三角形类型
bool judgeRT(float a, float b, float c) {
	return pow(a, 2) + pow(b, 2) == pow(c, 2);
}
void triangle() {
	float a, b, c = 1;
	while (1)
	{
		printf("输入三角形三边长用,分隔\n");
		scanf("%f,%f,%f", &a, &b, &c);
		if ((a + b <= c) || (a + c <= b) || (b + c <= a)) {
			printf("不构成三角形, 重新输入\n");
			continue;
		}
		else
		{
			if (judgeRT(a, b, c) || judgeRT(a, c, b) || judgeRT(b, c, a)) printf("是直角三角形\n");
			if (a == b && a ==c && b ==c) printf("是等边三角形\n");
			else if (a == b || a == c || b == c) printf("是等腰三角形\n");
			break;
		}
	}
}

// 判断剩余油量
void oilWatcher() {
	float oil = 0;
	printf("剩余油量\n");
	scanf("%f", &oil);
	if (oil < 0.25) printf("油量低，注意！\n");
	else if (oil >= 3.0 / 4.0) printf("高油量，不必停！\n");
}

// 输出小时和分钟
void hourMin() {
	int hour, min = 0;
	printf("输入小时和分钟用,分隔\n");
	scanf("%d,%d", &hour, &min);
	printf("%02d:%02d", hour, min);
}

// 四则运算器
void calculator() {
	char calcu = '+'; int a = 0, b = 0;
	printf("输入算式\n");
	scanf("%d%c%d", &a, &calcu, &b);
	switch (calcu) {
		default: printf("非四则运算符"); break;
		case '+': printf("%d%c%d=%d", a, calcu, b, a + b); break;
		case '-': printf("%d%c%d=%d", a, calcu, b, a - b); break;
		case '*': printf("%d%c%d=%d", a, calcu, b, a * b); break;
		case '/': printf("%d%c%d=%d", a, calcu, b, a / b); break;
	}
}

// 分数分级
void scoreSeperate() {
	int score = 0;
	printf("输入分数\n");
	scanf("%d", &score);
	switch (score / 10) {
		default: printf("不及格\n"); break;
		case 6: printf("及格\n"); break;
		case 7: printf("中等\n"); break;
		case 8: printf("良好\n"); break;
		case 9: case 10: printf("优秀\n"); break;
	}
}

// 输出某月有几天
void monthOutput() {
	int year = 0, month = 0, runMonth = 28;
	printf("输入年份和月份\n");
	scanf("%d %d", &year, &month);
	if (year % 4 == 0 && year % 100 != 0) runMonth = 29;
	switch (month) { 
		default: printf("本月30天"); break;
		case 1: case 3: case 5: case 7: case 8: case 10: case 12: printf("本月31天"); break;
		case 2:printf("本月%d天", runMonth); break;
	}
}