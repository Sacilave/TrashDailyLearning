#include <stdio.h>
#include <math.h>

// 计算 n 的阶乘
int factorial() {
	unsigned int n = 0, sum = 1;
	printf("输入 n：\n");
	scanf_s("%u", &n);
	for (int i = 1; i <= n; i++) { sum *= i; }
	printf("%u的阶乘为%u\n", n, sum);
}

// 计算 n 个 n 的阶乘相加
int nFactorial() {
	unsigned int n = 0, plusSum = 0, timeSum = 1;
	printf("输入 n：\n");
	scanf_s("%u", &n);
	for (int i = 1; i <= n; i++)
	{
		timeSum = 1;
		for (int j = 1; j <= i; j++) { timeSum *= j; }
		plusSum += timeSum;
	}
	printf("%u的各阶乘相加为%u\n", n, plusSum);
}


// 韩信点兵
int countNum() {
	int num = 0;
	while (1) { if ((num % 5 == 1) && (num % 6 == 5) && (num % 7 == 4) && (num % 11 == 10)) break; num++; }
	printf("有%d个兵\n", num);
}

// 判断素数
int judgePrime() {
	int PrimeNum = 0;
	printf("输入一个数字：\n");
	scanf_s("%d", &PrimeNum);
	for (int i = 2; i < PrimeNum; i++)
	{
		if (PrimeNum == 1) { printf("是素数\n"); break; }
		else if (PrimeNum % i != 0) continue;
		else printf("不是素数\n");  return 0;
	}
	printf("是素数\n");
}

// 猴子吃桃
int monkeyEating() {
	int peach = 1;
	for (int day = 0; day < 9; day++) { peach = 2 * (peach + 1); }
	printf("有%d个桃子\n", peach);
}

// 兔子
int recursion(int n) {
	if (n == 1 || n == 2) return 1;
	return recursion(n - 1) + recursion(n - 2);
}
int rabbitsBreed() { for (int i = 1; i <= 12; i++) { printf("%d 月共有兔子 %d 对\n", i, recursion(i)); } }