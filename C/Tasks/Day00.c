#define _CRT_SECURE_NO_WARNINGS 1;
#include<stdio.h>
#include<string.h>

int main2()
{
	char c[6] = "China"; int tmp;
	printf("��һ�⣺\n");
	for (int i = 0; i < 5; i++) {
		tmp = c[i] + 4;
		printf("'%c'��", tmp);
	}

	printf("\n�ڶ��⣺\n����һ���������ݣ�");
	int numGet, num01, result = 0;
	scanf("%d", &numGet);
	while (numGet > 0)
	{
		num01 = numGet % 10;
		result += num01;
		numGet /= 10;
	}
	printf("%d\n", result);

	double Area = 1; int r, h = 0; float PI = 3.1415;
	printf("��(1): Area = PI * r * r + 2 * PI * r * h\n����뾶:\n");
	scanf("%d", &r);
	printf("����߶ȣ�\n");
	scanf("%d", &h);
	Area = PI * r * r + 2 * PI * r * h;
	printf("Area = %lf\n\n", Area); 

	int Torque; int m1 = 1, m2 = 1, g = 1;
	printf("�ֱ����� m1��m2��g ��ֵ��\n");
	scanf("%d\n%d\n%d", &m1, &m2, &g);
	Torque = ((2 * m1 * m2) / (m1 + m2)) * g;
	printf("\nTorque = %d\n", Torque);
	
	
	int Side = 1, a, b, x;
	printf("�ֱ����� a��b��x ��ֵ��\n");
	scanf("%d\n%d\n%d", &a, &b, &x);
	Side = sqrt(a * a + b * b - 2 * a * b * cos(x));
	printf("\nSide = %d\n\n", Side);
	

	int Energy = 1, mass = 1, acceleration = 1, height = 1, velocity = 1;
	printf("�ֱ����� mass��acceleration��height, velocity ��ֵ��\n");
	scanf("%d\n%d\n%d\n%d", &mass, &acceleration, &height, &velocity);
	Energy = mass*(acceleration * height + velocity * velocity / 2);
	printf("\nEnergy = %d", Energy);
	
}
