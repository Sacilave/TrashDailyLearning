#include <iostream>

void testOutput();
void test03(int a);
void test03(char a) {
	std::cout << "abab" << std::endl;
}

int main() {
	test03('a');
}