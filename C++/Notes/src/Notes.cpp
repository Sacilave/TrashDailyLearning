#include <iostream>  // 预处理，在源文件被发送至编译器时，在编译之前就先处理这些预处理


void main2() {  // int main 函数无需设置返回值，默认返回 0，这仅对 main 适用
	std::cout << "hello world" << std::endl;  // 这个看起来像是左移位运算符的东西实际上是个函数，cout 这个函数
	std::cin.get();
}