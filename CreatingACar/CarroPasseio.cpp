#include <iostream>
#include "Motor.h"
#include "Veiculo.h"
#include "CarroPasseio.h"
#include "string.h"

using namespace std;

CarroPasseio::CarroPasseio()
{
    Cor = '\0';
    Modelo = '\0';
}

CarroPasseio::CarroPasseio (char *C, char *M, int NC, int PT, int KG, int VM, float PC): Motor (NC, PT) , Veiculo (KG, VM, PC)
{
    Cor = C;
    Modelo = M;
}

void CarroPasseio::set_Cor (char *C)
{
    Cor = C;
}
void CarroPasseio::set_Modelo (char *M)
{
    Modelo = M;
}

char *CarroPasseio::get_Cor ()
{
    return Cor;
}

char *CarroPasseio::get_Modelo ()
{
    return Modelo;
}

void CarroPasseio::get_data3()
{
    get_data1();
    get_data2();
    cout<<"Cor = " <<Cor <<endl;
    cout<<"Modelo = " <<Modelo <<endl;
}
