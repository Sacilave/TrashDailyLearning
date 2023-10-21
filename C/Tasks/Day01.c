#include <stdio.h>
#include <math.h>

void issue01() {  // ���� ���� �� ��ȣ�����������
	static int length, width;
	printf("���볤�Ϳ���,�ָ�\n");
	scanf("%d,%d", &length, &width);
	printf("�������Ϊ��%d\n", length * width);
}

void issue02() {  // ������İ뾶��������
	static float r; const float PI = 3.14;
	printf("������İ뾶��\n");
	scanf("%f", &r);
	printf("������Ϊ��%lf\n", 4 * PI * pow(r, 3) / 3);
}

void issue03() {  // ��������������� ƽ���� �� ��
	static float num01, num02, num03, ave, sum;
	printf("������������,�ָ�\n");
	scanf("%f,%f,%f", &num01, &num02, &num03);
	sum = num01 + num02 + num03;
	ave = sum / 3;
	printf("�������ĺ�Ϊ: %f\nƽ����Ϊ: %f\n", sum, ave);
}

void issue04() {  // �������������߳������ݺ��׹�ʽ������������
	static float line01, line02, line03, s, p;
	while (1)
	{
		printf("\n�������߳���,�ָ�\n");
		scanf("%f,%f,%f", &line01, &line02, &line03);
		if ((line01 + line02 <= line03) || (line01 + line03 <= line02) || (line02 + line03 <= line01)) {
			printf("����֮��δ���ڵ����ߣ�\n");
			continue;
		}
		else
		{
			p = (line01 + line02 + line03) / 2;
			s = sqrt(p * (p - line01) * (p - line02) * (p - line03));
			printf("\n���Ϊ%f", s);
			break;
		}
	}
}

void issue05() {  // ����һ�����������λ��˽��
	static int num04, numGet; int result = 1;
	printf("\n����һ������\n");
	scanf("%d", &numGet);
	while (numGet != 0)
	{
		result *= numGet % 10;
		numGet /= 10;
	}
	printf("��λ���Ϊ %d\n", result);
}

void issue06() {  // ���϶� ת ���϶�
	static float F;
	printf("����һ�������¶ȣ�\n");
	scanf("%f", &F);
	printf("ת��Ϊ���϶ȣ�%f\n", 5 * (F - 32) / 9);
}

void issue07() {  // ���ָ���ַ�
	char *columns[] = { "���", "����վ", "����վ" , "����ʱ��" , "����ʱ��" , "��ʱ" , "Ʊ��" , "��Ʊ����" };
	for (int i = 0; i < 8; i++) {
		printf(" ---------- |");
	};
	printf("\n");
	for (int i = 0; i < 8; i++) {
		printf(" %-10s |", columns[i]);
	}
}
