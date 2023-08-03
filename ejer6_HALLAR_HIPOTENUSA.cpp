#include <iostream>
#include <math.h> //LIBRERÍA PARA RAIZ Y POTENCIA
using namespace std;

//DECLARAR LA FUNCIÓN PARA HALLAR EL PRIMER CATETO
float pedir_catetos1(){
    float cateto1;
cout<<"Ingrese el cateto 1\n";
do{
    cin>>cateto1;
    if(cateto1<=0){
        cout<<"Ingrese un valor válido\n";
    }
}while(cateto1<=0);
return cateto1;
}
//FIN DE LA FUNCIÓN

//DECLARAR LA FUNCIÓN PARA HALLAR EL SEGUNDO CATETO
float pedir_catetos2(){
    float cateto2;
cout<<"Ingrese el cateto 2\n";
do{
    cin>>cateto2;
    if(cateto2<=0){
        cout<<"Ingrese un valor válido\n";
    }
}while(cateto2<=0);
return cateto2;
}
//FIN DE LA FUNCIÓN

//DECLARAR LA FUNCIÓN PARA HALLAR LA HIPOTENUSA
float hallar_hipotenusa(float cateto1,float cateto2){
float hipotenusa;
hipotenusa=sqrt(pow(cateto1,2)+pow(cateto2,2));
return hipotenusa;
}
//FIN DE LA FUNCIÓN

//FUNCIÓN PRINCIPAL
int main(){
    float cateto1,cateto2;
cateto1=pedir_catetos1(); //LLAMAR A LA FUNCIÓN PEDIR_CATETO1
cateto2=pedir_catetos2(); //LLAMAR A LA FUNCIÓN PEDIR_CATETO2
cout<<"La hipotenusa es: "<<hallar_hipotenusa(cateto1,cateto2); //LLAMAR A LA FUNCIÓN HALLAR_HIPOTENUSA
    return 0;

}