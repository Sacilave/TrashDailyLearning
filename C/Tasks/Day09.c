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
	for (int i = 0; i < 2; i++) { for (int j = 0; j < 3; j++) { arr[i][j] = i * 3 + j + 1; } }
	for (int i = 0; i < 2; i++) { for (int j = 0; j < 3; j++) { printf("%6d", arr[i][j]); } printf("\n"); }
	for (int i = 0; i < 3; i++) { for (int j = 0; j < 2; j++) { arrT[i][j] = arr[j][i]; } }  // T
	printf("array B: \n");
	for (int i = 0; i < 3; i++) { for (int j = 0; j < 2; j++) { printf("%6d", arrT[i][j]); } printf("\n"); }  // ��λΪ6ʱ�պ��������������Ŀ��һģһ��QWQ
}

// Arr max
void d9GetArrMax() {
	int arr[3][4]; int max = 0; int posI, posJ;
	for (int i = 0; i < 3; i++) { for (int j = 0; j < 4; j++) { arr[i][j] = i * 3 + j + 1; } }
	for (int i = 0; i < 3; i++) { for (int j = 0; j < 4; j++) { printf("%6d", arr[i][j]); } printf("\n"); }
	for (int i = 0; i < 3; i++) { for (int j = 0; j < 4; j++) { if (arr[i][j] > max) { max = arr[i][j]; posI = i + 1; posJ = j + 1; } } }
	printf("���Ϊ %d, �� %d �� �� %d ��\n", max, posI, posJ);
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
void d9OddDelete() {  // abcde�������е���������ᵼ��ûһ���������±��ֵ��Ϊ��ż������Ϊbdf...ÿ��ASCII��Ϊż������ace...ÿ�������ֶ��Ǹ�����Ц�����һ���Ϊ���㷨д���˵��˰���
	int length;	char trash;
	printf("�����ַ������ȣ�\n");
	scanf("%d", &length);
	scanf("%c", &trash);
	char str[50] = { NULL };
	for (int i = 0; i < length; i++)
	{
		char temp;
		scanf("%c", &temp);
		if (temp % 2 == 0) continue;
		else if (i % 2 == 0) continue;
		else str[i] = temp;
	}
	for (int i = 0; i < length; i++) { printf("%c ", str[i]); }
}

// arr size compare
void d9ArrSizeCmp() {
	char str1[30] = { NULL }, str2[] = "C Language"; int count = 0;
	for (int i = 0; i < 30; i++)
	{
		char temp;
		scanf("%c", &temp);
		if (temp == '\n') break;
		else 
		{
			count += 1;
			str1[i] = temp;
		}
	}
	if (count > 11) printf("strl>str2\n");
	else if (count == 11) printf("strl=str2\n");
	else printf("strl<str2\n");
}

// login 
int d9LoginJudge() {
	char pwd[] = "adninistrators"; int flag = 1;
	for (int i = 0; i < 14; i++)
	{
		char temp;
		scanf("%c", &temp);
		if (temp != pwd[i]) flag = 0;
	}
	return flag;
}
void d9Login() {
	printf("username: 123\nEnter password: ");
	if (d9LoginJudge() == 1) printf("OK\n");
	else {
		printf("Invalid password\n");
		printf("Enter passvord, again\n");
		d9Login();
	}
}

// frequency count
void d9FrequencyCount() {  // ���ǹ���ȡ�����ÿ�α����ж������Ƿ���� arr �У� ���ڼ�����������ռλ���������Ӱ��Ч�ʣ���Ϊ ����26 �Ķ�ά���飬�ڶ�ά���ڼ�����������Ϊ0��������������count
	int arr[26][2] = { 0 };
	while (1)
	{
		char temp;
		scanf("%c", &temp);
		if (temp == '\n') break;
		else if ((temp <= 90 && temp >= 65)) {  // ��д
			arr[temp - 65][1] += 1;
		}
		else if (temp <= 122 && temp >= 97) {  // Сд
			arr[temp - 97][1] += 1;
		}
	}
	for (int i = 0; i < 26; i++) { arr[i][0] = 65 + i; }
	for (int i = 0; i < 26; i++) { if (arr[i][1] != 0) printf("'%c': %d\n", arr[i][0], arr[i][1]); }
}