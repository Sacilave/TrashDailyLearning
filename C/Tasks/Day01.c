#include <stdio.h>
#include <math.h>

void issue01() {  // 输入 长度 和 宽度，输出矩形面积
	static int length, width;
	printf("输入长和宽用,分隔\n");
	scanf("%d,%d", &length, &width);
	printf("矩形面积为：%d\n", length * width);
}

void issue02() {  // 输入球的半径，输出体积
	static float r; const float PI = 3.14;
	printf("输入球的半径：\n");
	scanf("%f", &r);
	printf("球的体积为：%lf\n", 4 * PI * pow(r, 3) / 3);
}

void issue03() {  // 输入三个数，输出 平均数 和 和
	static float num01, num02, num03, ave, sum;
	printf("输入三个数以,分隔\n");
	scanf("%f,%f,%f", &num01, &num02, &num03);
	sum = num01 + num02 + num03;
	ave = sum / 3;
	printf("三个数的和为: %f\n平均数为: %f\n", sum, ave);
}

void issue04() {  // 输入三角形三边长，根据海伦公式输出三角形面积
	static float line01, line02, line03, s, p;
	while (1)
	{
		printf("\n输入三边长以,分隔\n");
		scanf("%f,%f,%f", &line01, &line02, &line03);
		if ((line01 + line02 <= line03) || (line01 + line03 <= line02) || (line02 + line03 <= line01)) {
			printf("两边之和未大于第三边！\n");
			continue;
		}
		else
		{
			p = (line01 + line02 + line03) / 2;
			s = sqrt(p * (p - line01) * (p - line02) * (p - line03));
			printf("\n面积为%f", s);
			break;
		}
	}
}

void issue05() {  // 输入一个数，输出各位相乘结果
	static int num04, numGet; int result = 1;
	printf("\n输入一个数：\n");
	scanf("%d", &numGet);
	while (numGet != 0)
	{
		result *= numGet % 10;
		numGet /= 10;
	}
	printf("各位相乘为 %d\n", result);
}

void issue06() {  // 华氏度 转 摄氏度
	static float F;
	printf("输入一个华氏温度：\n");
	scanf("%f", &F);
	printf("转换为摄氏度：%f\n", 5 * (F - 32) / 9);
}

void issue07() {  // 输出指定字符
	char *columns[] = { "班次", "出发站", "到达站" , "出发时间" , "到达时间" , "历时" , "票价" , "余票数量" };
	for (int i = 0; i < 8; i++) {
		printf(" ---------- |");
	};
	printf("\n");
	for (int i = 0; i < 8; i++) {
		printf(" %-10s |", columns[i]);
	}
}
