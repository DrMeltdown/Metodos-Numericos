#include <iostream>
#include <cmath>
using namespace std;
double e = 2.718281828459045090795598298427648842334747314453125;
double f(double x) {
    double función = pow(e,x) - pow(x, 2);
    return función;

}
int main() {
double a = -50;
double b = 40;
double p = 0;
int Max = 100;
double Tolerancia = 10e-16;
double FA = 0;
double FP = 0;
int i = 1;
bool root_found = false;
cout << "Buscando raiz de la funcion ingresada por medio de bisección..." << endl;
while (i <= Max and root_found == false) {
    p = a + ((b - a) / 2);
    FP = f(p);
    FA = f(a);
    if (p == 0 + Tolerancia or p == 0 - Tolerancia or (b - a) / 2 < Tolerancia) {
        cout << "Programa exitoso" << endl;
        printf("La raiz vale %.16f\n",p);
        cout << "Fueron requeridas " << i << " iteraciones para llegar al resultado";
        root_found = true;
        break;
    }
    else {
        i = i + 1;
    }
    if (FA * FP > 0) {
        a = p;
        FA = FP;
    }
    else {
        b = p;
    }
}
if (root_found == false) {
    cout<<"No se ha logrado encontrar una raíz" << endl;
    cout<<"Ejecución finalizada";
}
	return 0;
}