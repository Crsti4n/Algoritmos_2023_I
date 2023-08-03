#include <iostream>
using namespace std;

//DECLARANDO LA FUNCIÓN PARA PEDIR NOTA ACTITUDINAL
float pedir_notaActitudinal(){
    float nota_Actitudinal;
cout<<"Ingrese la nota actitudinal\n";
do{
    cin>>nota_Actitudinal;
    if(nota_Actitudinal<0|| nota_Actitudinal>20){
        cout<<"Ingrese una nota válida\n";
    }
}while(nota_Actitudinal<0|| nota_Actitudinal>20);
return nota_Actitudinal;
}
//FIN DE LA FUNCIÓN

//DECLARANDO LA FUNCIÓN PARA PEDIR NOTA FINAL
float pedir_notaFinal(){
    float nota_Final;
cout<<"Ingrese la nota final\n";
do{
    cin>>nota_Final;
    if(nota_Final<0|| nota_Final>20){
        cout<<"Ingrese una nota válida\n";
    }
}while(nota_Final<0|| nota_Final>20);
return nota_Final;
}
//FIN DE LA FUNCIÓN

//DECLARANDO LA FUNCIÓN PARA PEDIR NOTA PARCIAL
float pedir_notaParcial(){
    float nota_Parcial;
cout<<"Ingrese la nota parcial\n";
do{
    cin>>nota_Parcial;
    if(nota_Parcial<0|| nota_Parcial>20){
        cout<<"Ingrese una nota válida\n";
    }
}while(nota_Parcial<0|| nota_Parcial>20);
return nota_Parcial;
}
//FIN DE LA FUNCIÓN

//DECLARANDO LA FUNCIÓN PARA PEDIR NOTA DE PRÁCTICA
float pedir_notaPractica(){
    float nota_Practica;
cout<<"Ingrese la nota práctica\n";
do{
    cin>>nota_Practica;
    if(nota_Practica<0|| nota_Practica>20){
        cout<<"Ingrese una nota válida\n";
    }
}while(nota_Practica<0|| nota_Practica>20);
return nota_Practica;
}
//FIN DE LA FUNCIÓN

//DECLARANDO LA FUNCIÓN PARA PEDIR NOTA DE MEDIO CURSO
float pedir_notaMedioCurso(){
    float nota_MedioCurso;
cout<<"Ingrese la nota de medio curso\n";
do{
    cin>>nota_MedioCurso;
    if(nota_MedioCurso<0|| nota_MedioCurso>20){
        cout<<"Ingrese una nota válida\n";
    }
}while(nota_MedioCurso<0|| nota_MedioCurso>20);
return nota_MedioCurso;
}
//FIN DE LA FUNCIÓN

//DECLARANDO LA FUNCIÓN PARA PEDIR NOTA ENCARGADA
float pedir_notaEncargada(){
    float nota_Encargada;
cout<<"Ingrese la nota encargada\n";
do{
    cin>>nota_Encargada;
    if(nota_Encargada<0|| nota_Encargada>20){
        cout<<"Ingrese una nota válida\n";
    }
}while(nota_Encargada<0|| nota_Encargada>20);
return nota_Encargada;
}
//FIN DE LA FUNCIÓN

//DECLARANDO LA FUNCIÓN PARA HALLAR EL PROMEDIO PONDERADO
float hallar_promedio(float nota_Actitudinal, float nota_Final, float nota_Parcial, float nota_Practica, float nota_MedioCurso, float nota_Encargada){
    float promedio;
    promedio=nota_Actitudinal*0.05+nota_Practica*0.15+nota_Parcial*0.20+nota_Final*0.25+nota_MedioCurso*0.20+nota_Encargada*0.15;
    return promedio;
}
//FIN DE LA FUNCIÓN

int main(){
    float nota_Actitudinal,nota_Final,nota_Parcial,nota_Practica,nota_MedioCurso,nota_Encargada; //DECLARANDO VARIABLES PARA USARLAS DE PARÁMETROS
nota_Actitudinal=pedir_notaActitudinal(); //LLAMANDO A LA FUNCIÓN NOTA_ACTITUDINAL
nota_Final=pedir_notaFinal(); //LLAMANDO A LA FUNCIÓN NOTA_FINAL
nota_Parcial=pedir_notaParcial(); //LLAMANDO A LA FUNCIÓN NOTA_PARCIAL
nota_Practica=pedir_notaPractica(); //LLAMANDO A LA FUNCIÓN NOTA_PRACTICA
nota_MedioCurso=pedir_notaMedioCurso(); //LLAMANDO A LA FUNCIÓN NOTA_MEDIOCURSO
nota_Encargada=pedir_notaEncargada(); //LLAMANDO A LA FUNCIÓN NOTA_ENCARGADA

cout<<"La nota ponderada del alumno es "<<hallar_promedio(nota_Actitudinal,nota_Final,nota_Parcial,nota_Practica,nota_MedioCurso,nota_Encargada);
//LLAMANDO Y MOSTRANDO LA FUNCIÓN HALLAR_PROMEDIO

    return 0;
}