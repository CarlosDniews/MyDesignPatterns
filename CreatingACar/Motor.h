#ifndef MOTOR_H
#define MOTOR_H

using namespace std;

class Motor
{
    private:
        int NumCilindro;
        int Potencia;

    public:
        Motor();
        Motor (int NC, int P);
        void set_NumCilindro (int NC);
        void set_Potencia (int P);
        int get_NumCilindro ();
        int get_Potencia ();
        void get_data1 ();

    protected:


};

#endif // MOTOR_H
