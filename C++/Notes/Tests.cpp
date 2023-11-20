#include <iostream>

int a = 0;
void test03(char a) {
	std::cout << sizeof(a) << std::endl;
}

int main() {
	test03('a');
}