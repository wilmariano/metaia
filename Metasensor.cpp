#include "Metasensor.h"
Metasensor::Metasensor(int input) {
  this->input = input;
  init();
}
void Metasensor::init() {
  setCalibrate_bool();
}
void Metasensor::setCalibrate_bool() {
  delay(10000);
  Serial.print("0% value for what you are measuring will be...");
  x = analogRead(input);
  Serial.println(x);
  delay(10000);
  Serial.print("100% value for what you are measuring will be...");
  y = analogRead(input);
  Serial.println(y);
  Serial.println("If using MAP command, use X and Y values as reference.");
}
int Metasensor::getDifuse_read() {
  delay(10000);
  input = analogRead(input);
  Serial.println(input);
  output = map(input, y,x, 100, 0);
  Serial.print("Sensor get caught: ");
  Serial.print(output);
  Serial.println("%");
}
int Metasensor::getDifuse_read_specific(int a, int b) {
  delay(10000);
  Serial.print("Value a: ");
  Serial.println(a);
  Serial.print("Value b: ");
  Serial.println(b);
  delay(10000);
  input = analogRead(input);
  Serial.println(input);
  int output_specific = map(input, b,a, 100, 0);
  return output_specific;
}
