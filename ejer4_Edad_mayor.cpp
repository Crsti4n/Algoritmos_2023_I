#include <iostream>
using namespace std;

// Función para obtener la edad mayor y la diferencia entre dos edades
int ObtenerEdadMayor(int edad1, int edad2, int& diferencia) {
    int mayor;
    if (edad1 > edad2) {
        mayor = edad1;
        diferencia = edad1 - edad2;
    } else {
        mayor = edad2;
        diferencia = edad2 - edad1;
    }
    return mayor;
}

// Función principal (Main)
int main() {
    int edad1, edad2, mayor, diferencia;

    // Obtener la primera edad desde el usuario
    cout << "Ingrese edad 1: ";
    cin >> edad1;

    // Obtener la segunda edad desde el usuario
    cout << "Ingrese edad 2: ";
    cin >> edad2;

    // Obtener la edad mayor y la diferencia llamando a la función ObtenerEdadMayor
    mayor = ObtenerEdadMayor(edad1, edad2, diferencia);

    // Mostrar el resultado
    cout << "El mayor tiene: " << mayor << " años, tiene " << diferencia << " años de diferencia con el menor" << endl;

    return 0;
}
