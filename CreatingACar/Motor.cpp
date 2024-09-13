#include <iostream>
#include "Motor.h"

using namespace std;

Motor::Motor ()
{
    NumCilindro = 0;
    Potencia = 0;
}

Motor::Motor(int NC, int P)
{
    NumCilindro = NC;
    Potencia = P;
}

void Motor::set_NumCilindro (int NC)
{
    NumCilindro = NC;
}

void Motor::set_Potencia (int P)
{
    Potencia = P;
}

int Motor::get_NumCilindro()
{
    return NumCilindro;
}

int Motor::get_Potencia()
{
    return Potencia;
}

void Motor::get_data1 ()
{
    cout<<"Num.Cilindr = " <<NumCilindro <<endl;
    cout<<"Potencia = " <<Potencia <<endl;
}
