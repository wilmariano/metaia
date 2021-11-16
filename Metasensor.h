#ifndef METASENSOR_H
#define METASENSOR_H

#include <Arduino.h>

//  https://roboticsbackend.com/arduino-create-library/

class Metasensor {
  
  private:
    int input;
    int output;
    int x;
    int y;
    
  public:
    // Chama o método Metasensor e nele declaro o input e chamo init()
    Metasensor(int input);

    // Comando de chamada do init()
    // and power off the LED - default state
    void init();
    
    // Método de calibrar sensor
    void setCalibrate_bool();

    // Leitor do valor analógico de acordo com calibrado anteriormente
    int getDifuse_read();

    // Leitor do valor analógico de acordo com valor recebido
    int getDifuse_read_specific(int a, int b);

    // Método de calibrar sensor de umidade solo - CAPACITIVO
    void setSensor_Umidade_Capacitivo();

    // Leitor do valor analógico de acordo com calibrado anteriormente - CAPACITIVO
    int getSensor_Umidade_Capacitivo(int a, int b);
};

#endif