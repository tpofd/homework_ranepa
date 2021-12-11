// pz6.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Russian");
    int choice;
    double y1 = 0, y2 = 0, y3 = 0;
    double a, b, z, x;
    double pi = 3.14;

    cout << "Выберете одну из следующих функций:" << endl;
    cout << "1. y = a*ln(1+x^1/5)+cos^[fi(x)+1]" << endl;
    cout << "2. y = (2 * a * fi(x) + b * cos(sqrt(|x|))" << endl;
    cout << "3. y = pi * fi(x) + a * cos^2(x^3) + b * sin^3(x^2)" << endl;
    cout << "4. y = 2 * a * cos^3(x^2) + sin^2(x^3) - b * fi(x)" << endl;
    cout << "5. y = a * fi(x) - ln(x + 2,5) + b(e^x - e^(-x))" << endl;
    cout << "Ваш выбор? ";
    cin >> choice;

    switch (choice)
    {
    case 1:
        cout << "Введите a: ";
        cin >> a;
        cout << "Введите z: ";
        cin >> z;

        if (z < 1) {
            x = z * z;
        }
        else {
            x = z + 1;
        }

        y1 = a * log(1 + pow(x, 0.2)) + pow(cos(2 * x + 1), 2);
        y2 = a * log(1 + pow(x, 0.2)) + pow(cos(x * x + 1), 2);
        y3 = a * log(1 + pow(x, 0.2)) + pow(cos(x / 3 + 1), 2);

        break;
    case 2:
        cout << "Введите a: ";
        cin >> a;
        cout << "Введите b: ";
        cin >> b;
        cout << "Введите z: ";
        cin >> z;

        if (z < 1) {
            x = 2 + z;
        }
        else {
            x = pow(sin(z), 2);
        }

        y1 = (2 * a * 2 * x + b * cos(sqrt(abs(x)))) / (x * x + 5);
        y2 = (2 * a * x * x + b * cos(sqrt(abs(x)))) / (x * x + 5);
        y3 = (2 * a * x / 3 + b * cos(sqrt(abs(x)))) / (x * x + 5);

        break;
    case 3:
        cout << "Введите a: ";
        cin >> a;
        cout << "Введите b: ";
        cin >> b;
        cout << "Введите z: ";
        cin >> z;
        
        if (z < 1) {
            x = z;
        }
        else {
            x = sqrt(pow(z, 3));
        }

        y1 = -1 * pi * 2 * x + a * pow(cos(pow(x, 3)), 2) + b * pow(sin(x * x), 3);
        y2 = -1 * pi * x * x + a * pow(cos(pow(x, 3)), 2) + b * pow(sin(x * x), 3);
        y3 = -1 * pi * x / 3  + a * pow(cos(pow(x, 3)), 2) + b * pow(sin(x * x), 3);

        break;
    case 4:
        cout << "Введите a: ";
        cin >> a;
        cout << "Введите b: ";
        cin >> b;
        cout << "Введите z: ";
        cin >> z;

        if (z < 1) {
            x = pow(z, 3) + 0.2;
        }
        else {
            x = z + log(z);
        }

        y1 = 2 * a * pow(cos(x * x), 3) + pow(sin(pow(x, 3)), 2) - b * 2 * x;
        y2 = 2 * a * pow(cos(x * x), 3) + pow(sin(pow(x, 3)), 2) - b * x * x;
        y3 = 2 * a * pow(cos(x * x), 3) + pow(sin(pow(x, 3)), 2) - b * x / 3;

        break;
    case 5:
        cout << "Введите a: ";
        cin >> a;
        cout << "Введите b: ";
        cin >> b;
        cout << "Введите z: ";
        cin >> z;

        if (z < -1) {
            x = -z / 3;
        }
        else {
            x = abs(z);
        }

        y1 = a * 2 * x - log(x + 2.5) + b * (exp(x) - exp(-x));
        y2 = a * x * x - log(x + 2.5) + b * (exp(x) - exp(-x));
        y3 = a * x / 3 - log(x + 2.5) + b * (exp(x) - exp(-x));

        break;
    default:
        cout << "Такая функция не найдена, попробуйте еще раз" << endl;
        break;
    }

    cout << "При fi(x) = 2x, y = " << y1 << endl;
    cout << "При fi(x) = x^2, y = " << y2 << endl;
    cout << "При fi(x) = x/3, y = " << y3 << endl;
}

// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
