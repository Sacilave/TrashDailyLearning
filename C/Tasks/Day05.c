#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <windows.h>

int d5Factorial(int n) {
	int output = 1;
	for (int i = 1; i < n+1; i++) { output *= i; }
	return output;
}

void d5Task01() {
	int m, n, res;
	printf("分别输入 m 和 n：\n");
	scanf("%d%d", &m, &n);
	res = d5Factorial(n) / d5Factorial(m) / d5Factorial(n - m);
	printf("结果为 %d\n", res);
}

int d5Min(int a, int b) {
	if (a < b) return a;
	else return b;
}

void d5Task02() {
	int a, b, c;
	printf("输入三个数\n");
	scanf("%d%d%d", &a, &b, &c);
	printf("最小的数是 %d\n", d5Min(d5Min(a, b), c));
}

int d5isPrime(int num) {
	if (num == 1) return 1;
	else
	{
		for (int i = 2; i < num; i++)
		{
			if (num % i == 0) return 0;
		}
		return 1;
	}
}
// 素数
void d5Task03() {
	int sum = 0;
	for (int i = 1; i <= 1000; i++)
	{
		if (d5isPrime(i) == 1) { 
			printf("%d ", i); 
			sum++; 
			if (sum % 8 == 0) printf("\n");
		}
	}
	printf("\n");
}

int d5Max(int a, int b) {
	if (a > b) return a;
	else return b;
}

int gcd(int a, int b) {
	int res = NULL;
	for (int i = 1; i < d5Max(a, b); i++) { if (a % i == 0 && b % i == 0) res = i; }
	return res;
}
int lcm(int a, int b) {
	return a * b / gcd(a, b);
}
void d5Task04() {
	int a, b;
	printf("输入两个数字\n");
	scanf("%d%d", &a, &b);
	printf("最大公约数为：%d\t最小公倍数为：%d\n", gcd(a, b), lcm(a, b));
}

// x 的 n 次幂
int d5pow(int x, int n) {
	if (n == 1) { return x; }
	return x * d5pow(x, n-1);
}

void d5Task05() {
	int x, n;
	printf("输入 x 和 n\n");
	scanf("%d%d", &x, &n);
	printf("%d 的 %d 次幂为：%d\n", x, n, d5pow(2, 3));
}

// 菜单
void d5Task06() {
	Sleep(5000);
	int command, n;
	float num;
	system("cls");
	printf("======= MENU =======\n fabs···········1\n sqrt···········2\n pow············3\n sin············4\n exit···········5\n====================\n");
	scanf("%d", &command);
	switch (command)
	{
	default:
		printf("输错啦");
		Sleep(500);
		d5Task06();
		break;
	case 1:
		printf("请输入一个数:\n");
		scanf("%f", &num);
		printf("%f 的绝对值为%f", num, fabs(num));
		break;
	case 2:
		printf("请输入一个数:\n");
		scanf("%f", &num);
		printf("%f 的开根为%f", num, sqrt(num));
		break;
	case 3:
		printf("请输入两个数:\n");
		scanf("%f%d", &num, &n);
		printf("%f 的 %d 次幂为 %f", num, n, pow(num, n));
		break;
	case 4:
		printf("请输入一个数:\n");
		scanf("%f", &num);
		printf("%f 的正弦为%f", num, sin(num));
		break;
	case 5:
		printf("退出中...\n");
		return;
	}
}

int main() {
	d5Task01(); d5Task02(); d5Task03(); d5Task04(); d5Task05(); d5Task06();
}