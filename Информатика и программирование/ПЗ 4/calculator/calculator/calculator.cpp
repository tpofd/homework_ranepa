#include <iostream>
#include <locale.h>
#include <cstdlib>
#include <windows.h>
using namespace std;

int main() {
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	setlocale(LC_ALL, "RUS");
	
	int a, b;

	cout << "Введите первое число: ";
	cin >> a;
	cout << "Введите второе число: ";
	cin >> b;

	int c = a + b;
	cout << "Сумма чисел = " << c << endl;
	cout << "Разность чисел = " << a - b << endl;
	cout << "Умножение чисел = " << a * b << endl;

	system("pause");
}