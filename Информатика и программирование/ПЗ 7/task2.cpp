#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Russian");

    int points = 0, choice, res;

    cout << "1) How many cat lives?" << endl;
    cout << "answers: \n -> 5 lives \n -> 7 lives \n -> 9 lives" << endl;
    cout << "your answer: ";
    cin >> choice;

    if (choice == 9) points++;

    cout << "2) How many centimeters in a meter?" << endl;
    cout << "answers: \n -> 10 centimeters \n -> 100 centimeters \n -> 1000 centimeters" << endl;
    cout << "your answer: ";
    cin >> choice;

    if (choice == 100) points++;

    cout << "3) The speed of sound?" << endl;
    cout << "answers: \n -> 340 m/s \n -> 320 m/s \n -> 240 m/s" << endl;
    cout << "your answer: ";
    cin >> choice;

    if (choice == 340) points++;

    switch (points)
    {
    case 0:
        res = 2;
        break;
    case 1:
        res = 3;
        break;
    case 2:
        res = 4;
        break;
    case 3:
        res = 5;
        break;
    default:
        break;
    }

    cout << "Rating = " << res << " ballov";
}