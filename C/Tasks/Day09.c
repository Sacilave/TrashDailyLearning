#include <stdio.h>

// 13��ȥ��max��min����Average
void d9Rank() {
	int max = 0, min = 0, flagMin = 1, flagMax = 1, res = 0; int arr[13] = { 0 };
	for (int i = 0; i < 13; i++)
	{
		int temp;
		scanf("%d", &temp);
		if (temp > max) max = temp;
		if (temp < min) min = temp;
		arr[i] = temp;
	}
	for (int i = 0; i < 13; i++)
	{
		if (arr[i] == max && flagMax == 1) continue;
		else if (arr[i] == min && flagMin == 1) continue;
		else res += arr[i];
	}
	res /= 11;
	printf("%d", res);
}

// ��ά��������
void d9LayoutArr() {
	int arr[3][4] = {0};
	for (int i = 0; i < 3; i++) { for (int j = 0; j < 4; j++) { scanf("%d", &arr[i][j]);} }
	for (int i = 0; i < 3; i++) { for (int j = 0; j < 4; j++) { printf("%2d\t", arr[i][j]); } printf("\n"); }
}

// ת��
void d9T() {
	int arr[2][3], arrT[3][2];
	printf("array A: \n");
	for (int i = 0; i < 2; i++) { for (int j = 0; j < 3; j++) { arr[i][j] = i * 3 + j + 1; } }  // ��ֵ
	for (int i = 0; i < 2; i++) { for (int j = 0; j < 3; j++) { printf("%6d", arr[i][j]); } printf("\n"); }  // output
	for (int i = 0; i < 3; i++) { for (int j = 0; j < 2; j++) { arrT[i][j] = arr[j][i]; } }  // T
	printf("array B: \n");
	for (int i = 0; i < 3; i++) { for (int j = 0; j < 2; j++) { printf("%6d", arrT[i][j]); } printf("\n"); }  // ��λΪ6ʱ�պ�����ĸ���Ŀ��һģһ��QWQ
}

// ����
void d9Diamond() {
	char arr[5][5];
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			if (((i == 0 || i == 4) && j == 2) || ((i == 1 || i == 3) && (j == 1 || j == 3)) || (i == 2 && (j == 0 || j == 4))) arr[i][j] = '*';
			else arr[i][j] = ' ';
		}
	}
	for (int i = 0; i < 5; i++) { for (int j = 0; j < 5; j++) { printf("%c", arr[i][j]); } printf("\n"); }  // output
}

// delet odd nums
void d9OddDelete() {
	int length;	char temp;
	printf("�����ַ������ȣ�\n");
	scanf("%d", &length);
	scanf("%c", &temp);
	char str[50] = { NULL };
	for (int i = 0; i < length; i++)
	{
		scanf("%c", &temp);
		if (temp % 2 != 0) str[i] = temp;
	}
	for (int i = 0; i < length; i++)
	{
		printf("%c\t", str[i]);
	}
}


int main() {
	d9OddDelete();
}