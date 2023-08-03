#include <iostream>
using namespace std;

//DECLANDO FUNCIÓN PARA PEDIR DATOS AL USUARIO
int pedir_datos() {
    int N;
    cout << "Ingrese la cantidad de valores: ";
    do {
        cin >> N;
        if (N <= 0) {
            cout << "Ingrese un valor mayor o igual a cero: ";
        }
    } while (N <= 0);
    return N;
}
//FIN DE LA FUNCIÓN

//DECLANDO FUNCIÓN PARA HALLAR LOS DOS NÚMEROS MAYORES
void hallar_mayores(int N) {
    float mayor1, mayor2, num;
    cout << "Ingrese el 1° dato: ";
    cin >> num;
    mayor1 = num;
    mayor2 = num;
    for (int i = 2; i <= N; i++) {
        cout << "Ingrese el " << i << "° dato: ";
        cin >> num;
        if (num > mayor1) {
            mayor2 = mayor1;
            mayor1 = num;
        } else {
            if (num > mayor2) {
                mayor2 = num;
            }
        }
    }
    cout << "El número mayor es: " << mayor1 << endl;
    cout << "El segundo número mayor es: " << mayor2 << endl;
}
//FIN DE LA FUNCIÓN

//FUNCIÓN PRINCIPAL
int main() {
     int parametro=pedir_datos(); //LLAMANDO A LA FUNCIÓN PEDIR_DATOS Y ASIGNANDOLE UN VALOR
    hallar_mayores(parametro); //LLAMANDO A LA FUNCIÓN HALLAR_MAYORES 
    return 0;
}