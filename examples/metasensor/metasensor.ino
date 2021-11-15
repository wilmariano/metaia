#include <Metasensor.h>
Metasensor var(0);
void setup() 
{
  Serial.begin(115200);
}
void loop() {
  // var.init();
  // int res = var.getDifuse_read();
  // Serial.print("O valor é: ");
  // Serial.println(res);
  int res2 = var.getDifuse_read_specific(1023, 500);
  Serial.print("O valor é: ");
  Serial.println(res2);  
}
