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


void main() {
	Log log;
	log.SetLevel(log.LogLevelWarning);
	log.Warning("Hello!");

}