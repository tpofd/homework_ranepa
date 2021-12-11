#include <iostream>
#include <locale.h>
#include <cstdlib>
#include <windows.h>
using namespace std;

int main() {
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	setlocale(LC_ALL, "RUS");
	string name;

	cout << "Введите свое имя: ";
	cin >> name;
	cout << "Привет, " << name;

	system("pause");
}