#include <iostream>

using namespace std;

// Función para calcular el factorial de un número
int CalcularFactorial(int numero) {
    int factorial = 1;
    for (int i = 1; i <= numero; i++) {
        factorial *= i;
    }
    return factorial;
}

// Función principal (Main)
int main() {
    int numero1, factorial;

    // Obtener el número desde el usuario
    cout << "Ingrese número que desea calcular su factorial: ";
    cin >> numero1;

    // Calcular el factorial llamando a la función CalcularFactorial
    factorial = CalcularFactorial(numero1);

    // Mostrar el resultado del factorial
    cout << "El factorial es: " << factorial << endl;

    return 0;
}
