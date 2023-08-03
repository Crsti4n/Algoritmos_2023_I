#include <iostream>
using namespace std;

//DECLARAR UNA FUNCIÓN PARA PEDIR LOS GRADOS CELSIUS INGRESADOS POR EL USUARIO
float pedir_grados(){
    float grados;
cout<<"Ingrese los grados celsius\n";
cin>>grados;
return grados;
}
//FIN DE LA FUNCIÓN

//DECLARAR UNA FUNCIÓN PARA CONVERTIR LOS GRADOS CELSIUS A FARHENHEIT
float conversion_Farhenheit(float grados){
float conversion;
conversion=(9*grados-160)/5;
return conversion;
}
//FIN DE LA FUNCIÓN

//DECLARAR UNA FUNCIÓN PARA CONVERTIR LOS GRADOS CELSIUS A KELVIN
float conversion_Kelvin(float grados){
float conversion;
conversion=grados+273;
return conversion;
}
//FIN DE LA FUNCIÓN

//FUNCIÓN PRINCIPAL
int main(){
    int elegir; //DECLARANDO VALORES
float grados; //DECLARAR PARA USARLO EN EL PARÁMETRO
grados= pedir_grados();


//BLUCE PARA REPETIR EL MENÚ EN CASO DE ELECCIÓN INCORRECTA
do{
    
cout<<"Eliga una opción\n";
cout<<"1.Celsius a Farhenheit\n";
cout<<"2.Celsius a Kelvin\n";
cout<<"3.Salir\n";
cin>>elegir;

//SWITCH PARA MOSTRAR LA OPCIÓN ELEGIDA
switch(elegir){
case 1:
//MOSTRAR EL RESULTADO DE LA FUNCIÓN CONVERSION_FAHRENHEIT
cout<<"La temperatura en Farhenheit es: "<<conversion_Farhenheit(grados);
break;
case 2:
//MOSTRAR EL RESULTADO DE LA FUNCIÓN CONVERSION_KELVIN
cout<<" La temperatura en Kelvin es: "<<conversion_Kelvin(grados);
break;
case 3:
//OPCION PARA SALIR
cout<<"Hasta luego\n";
break;
default:
//EN CASO DE NO ELEGIR CORRECTAMENTE
cout<<"Ingrese opción válida\n";
break;
}
}while(elegir!=1 &&  elegir!=2 && elegir!=3);
    return 0;
}