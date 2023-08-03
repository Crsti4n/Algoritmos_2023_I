#include <iostream>
using namespace std;

// Función para verificar si un número es par o impar
bool VerificarPar(int numero) {
    if (numero % 2 == 0) {
        return true; // Es par
    } else {
        return false; // Es impar
    }
}

// Función principal (Main)
int main() {
    int numero;
    
    // Obtener el número desde el usuario
    cout << "Ingrese un número: ";
    cin >> numero;

    // Verificar si es par o impar llamando a la función VerificarPar
    if (VerificarPar(numero)) {
        cout << "El número es par" << endl;
    } else {
        cout << "El número es impar" << endl;
    }

    return 0;
}
