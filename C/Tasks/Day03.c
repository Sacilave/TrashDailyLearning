#include <stdio.h>
#include <math.h>

// ���� n �Ľ׳�
int factorial() {
	unsigned int n = 0, sum = 1;
	printf("���� n��\n");
	scanf_s("%u", &n);
	for (int i = 1; i <= n; i++) { sum *= i; }
	printf("%u�Ľ׳�Ϊ%u\n", n, sum);
}

// ���� n �� n �Ľ׳����
int nFactorial() {
	unsigned int n = 0, plusSum = 0, timeSum = 1;
	printf("���� n��\n");
	scanf_s("%u", &n);
	for (int i = 1; i <= n; i++)
	{
		timeSum = 1;
		for (int j = 1; j <= i; j++) { timeSum *= j; }
		plusSum += timeSum;
	}
	printf("%u�ĸ��׳����Ϊ%u\n", n, plusSum);
}


// ���ŵ��
int countNum() {
	int num = 0;
	while (1) { if ((num % 5 == 1) && (num % 6 == 5) && (num % 7 == 4) && (num % 11 == 10)) break; num++; }
	printf("��%d����\n", num);
}

// �ж�����
int judgePrime() {
	int PrimeNum = 0;
	printf("����һ�����֣�\n");
	scanf_s("%d", &PrimeNum);
	for (int i = 2; i < PrimeNum; i++)
	{
		if (PrimeNum == 1) { printf("������\n"); break; }
		else if (PrimeNum % i != 0) continue;
		else printf("��������\n");  return 0;
	}
	printf("������\n");
}

// ���ӳ���
int monkeyEating() {
	int peach = 1;
	for (int day = 0; day < 9; day++) { peach = 2 * (peach + 1); }
	printf("��%d������\n", peach);
}

// ����
int recursion(int n) {
	if (n == 1 || n == 2) return 1;
	return recursion(n - 1) + recursion(n - 2);
}
int rabbitsBreed() { for (int i = 1; i <= 12; i++) { printf("%d �¹������� %d ��\n", i, recursion(i)); } }