#include <stdio.h>

// max number
void d7MaxNum() {
	int temp = 0, input;
	while (1)
	{
		scanf("%d", &input);
		if (input == 0) break;
		else {
			if (input > temp) temp = input;
		}
	}
	printf("%d\n", temp);
}

// list sum
void d7ListSum() {
	int n; float sum = 0.0;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) { sum += 1.0 / (3.0 * i - 2.0); }
	printf("%f\n", sum);
}

// watermelon
void d7Watermelon() {
	int num, count = 0;
	scanf("%d", &num);
	while (num > 0) {
		num = num / 2 - 2;
		count++;
	}
	printf("%d\n", count);
}

// grade judge
void d7GradeJudge() {
	int repeat, grade;
	scanf("%d", &repeat);
	for (int i = 0; i < repeat; i++)
	{
		scanf("%d", &grade);
		if (grade < 60) printf("Fail\n");
		else printf("Pass\n");
	}
}

// tax
void d7Tax() {
	int times, income = 0;
	scanf("%d", &times);
	for (int i = 0; i < times; i++)
	{
		scanf("%d", &income);
		if (income <= 1000) printf("%d ", 0);
		else if (income <= 3000) printf("%d ", income *= 0.03);
		else if (income <= 5000) printf("%d ", income *= 0.04);
		else printf("%d ", income *= 0.06);
	}
	printf("\n");
}

// muti num
void d7MutiNum() {
	int num, count = 0;
	scanf("%d", &num);
	for (int i = 1; i <= num; i++)
	{
		if (num % i == 0) count++;
	}
	printf("%d\n", count);
}

// max muti num
void d7MaxMutiNum() {
	int m, n, temp, maxNum;
	scanf("%d%d", &m, &n);
	if (m > n) {
		temp = n;
		n = m;
		m = temp;
	}
	for (int i = 1; i <= n; i++)
	{
		if (n % i == 0 && m % i == 0) maxNum = i;
	}
	printf("%d", maxNum);
}