#include <iostream>
using namespace std;

//FUNCIÓN PARA PEDIR LA CANTIDAD DE HOMBRES
int pedir_cantidadHombres(){
    int cantidad_hombres;
cout<<"Ingrese la cantidad de hombres\n";
do{
    cin>>cantidad_hombres;
    if(cantidad_hombres<0){
        cout<<"Ingrese una cantidad válida de personas\n";
    }
}while(cantidad_hombres<0);
return cantidad_hombres;
}
//FIN DE LA FUNCIÓN

//FUNCIÓN PARA PEDIR LA CANTIDAD DE MUJERES
int pedir_cantidadMujeres(){
    int cantidad_mujeres;
cout<<"Ingrese la cantidad de mujeres\n";
do{
    cin>>cantidad_mujeres;
    if(cantidad_mujeres<0){
        cout<<"Ingrese una cantidad válida de personas\n";
    }
}while(cantidad_mujeres<0);
return cantidad_mujeres;
}
//FIN DE LA FUNCIÓN

//FUNCIÓN PARA HALLAR EL PORCENTAJE DE HOMBRES
float hallar_porcentajeHombres(int cantidad_hombres, int cantidad_mujeres){
float porcentaje_hombres;
porcentaje_hombres=static_cast<float>(cantidad_hombres)/(cantidad_hombres+cantidad_mujeres)*100;
return porcentaje_hombres;
}
//FIN DE LA FUNCIÓN

//FUNCIÓN PARA PEDIR EL PORCENTAJE DE MUJERES
float hallar_porcentajeMujeres(int cantidad_hombres, int cantidad_mujeres){
float porcentaje_mujeres;
porcentaje_mujeres=static_cast<float>(cantidad_mujeres)/(cantidad_hombres+cantidad_mujeres)*100;
return porcentaje_mujeres;
}
//FIN DE LA FUNCIÓN
int main(){
int cantidad_hombres,cantidad_mujeres; //DECLARANDO VALORES PARA LOS PARÁMETROS
cantidad_hombres=pedir_cantidadHombres(); //LLAMANDO A LA FUNCIÓN PEDIR_CANTIDADHOMBRES
cantidad_mujeres=pedir_cantidadMujeres(); //LLAMANDO A LA FUNCIÓN PEDIR_CANTIDADMUJERES
cout<<endl;
cout<<"El porcentaje de hombres es de "<<hallar_porcentajeHombres(cantidad_hombres,cantidad_mujeres)<<"%"<<endl;
cout<<"El porcentaje de mujeres es de "<<hallar_porcentajeMujeres(cantidad_hombres,cantidad_mujeres)<<"%"<<endl;
//LLAMANDO Y MOSTRANDO LAS FUNCIONES HALLAR_PORCENTAJEHOMBRES Y HALLAR_PORCENTAJEMUJRES
    return 0;
}