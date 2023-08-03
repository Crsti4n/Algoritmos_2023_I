#include <iostream>
using namespace std;

// Función para calcular el precio final después de aplicar el descuento
float CalcularPrecioFinal(float precioOriginal, float porcentajeDescuento) {
    float descuento = (precioOriginal * porcentajeDescuento) / 100;
    float precioFinal = precioOriginal - descuento;
    return precioFinal;
}

// Función principal (Main)
int main() {
    float precioOriginal, porcentajeDescuento, precioConDescuento;

    // Obtener el precio original desde el usuario
    cout << "Ingrese el Precio: ";
    cin >> precioOriginal;

    // Obtener el porcentaje de descuento desde el usuario
    cout << "Ingrese el Descuento a aplicar (%): ";
    cin >> porcentajeDescuento;

    // Llamar a la función para calcular el precio final con el descuento
    precioConDescuento = CalcularPrecioFinal(precioOriginal, porcentajeDescuento);

    // Mostrar el precio final con el descuento
    cout << "El precio final con descuento es: " << precioConDescuento << endl;

    return 0;
}
