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

	cout << "������� ������ �����: ";
	cin >> a;
	cout << "������� ������ �����: ";
	cin >> b;

	int c = a + b;
	cout << "����� ����� = " << c << endl;
	cout << "�������� ����� = " << a - b << endl;
	cout << "��������� ����� = " << a * b << endl;

	system("pause");
}