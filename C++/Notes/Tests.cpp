#include <iostream>

void increasement(int& a) {
	a++;
}

class Log
{
public:
	const int LogLevelError = 0;
	const int LogLevelWarning = 1;
	const int LogLevelInfo = 2;
private:
	int m_LogLevel;
public:
	void SetLevel(int level) {
		m_LogLevel = level;
	}
	void Warning(const char* message) {
		if (m_LogLevel >= LogLevelWarning)
			std::cout << "[WARNING]:" << message << std::endl;
	}
	void Error(const char* message) {
		if (m_LogLevel >= LogLevelError)
			std::cout << "[Error]:" << message << std::endl;
	}
	void Info(const char* message) {
		if (m_LogLevel >= LogLevelInfo)
			std::cout << "[Info]:" << message << std::endl;
	}

};

struct Entity {
	static int a, b;
	int c, d;
	static void Print() {
		std::cout << a << ", " << b << std::endl;
	}
};

void main() {
	Entity en01, en02;

	en01.a = 3;
	Entity::b = 4;
	en01.a = 4;
	Entity::b = 5;
	en01.Print();

}