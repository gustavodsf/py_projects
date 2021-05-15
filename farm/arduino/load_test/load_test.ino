/*
     Q0481-Sketch-Calibrar
     AUTOR:   BrincandoComIdeias
     LINK:    https://www.youtube.com/brincandocomideias ; https://cursodearduino.net/
     COMPRE:  https://www.arducore.com.br/
     SKETCH:  Calibrar Balanca com módulo HX711
     DATA:    04/07/2019
*/

// INCLUSÃO DE BIBLIOTECAS
#include <Wire.h> // Library for I2C communication
#include <LiquidCrystal_I2C.h> // Library for LCD
#include <string.h>
#include <HX711.h>

// DEFINIÇÕES DE PINOS
#define pinDT  2
#define pinSCK  3
#define pesoMin -0.006
#define pesoMax 150.0
#define fatorEscala -10479.58896



#define qtdLeituras 5

LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x3F, 16, 2);

// INSTANCIANDO OBJETOS
HX711 scale;

// DECLARAÇÃO DE VARIÁVEIS
float medida = 0;
int i = 1;

void setup() {
  lcd.begin();
  lcd.backlight();
  
  Serial.begin(57600);
  show_init_message();
  scale.begin(pinDT, pinSCK); // CONFIGURANDO OS PINOS DA BALANÇA
  scale.set_scale(fatorEscala);
  delay(1000);
  scale.tare(); // ZERANDO A BALANÇA PARA DESCONSIDERAR A MASSA DA ESTRUTURA
}

void show_init_message(){
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Sta. Terezinha");
  lcd.setCursor(0, 1);
  lcd.print("Inicializando");
}

void show_weight_message(float medida){
  char LCDmsg[16];
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Sta. Terezinha");
  lcd.setCursor(0, 1);
  sprintf(LCDmsg, "Peso: %d.%03d Kg", (int)medida, (int)(medida*1000)%1000);
  lcd.print(LCDmsg);
}

void loop() {
  scale.power_up();
  medida = scale.get_units(qtdLeituras);
  if (medida <= pesoMin ){ 
    medida = 0.0; 
    //scale.tare(); 
    Serial.println("Tara Configurada!");
  } else if ( medida >= pesoMax ){
    medida = 0.0;  
    Serial.println("Tara Configurada!");
    //scale.tare(); 
  }
  medida = (medida < 0 ? 0.0 : medida);
  show_weight_message(medida);
  Serial.println(medida,3);  
  scale.power_down();
  delay(100); 
  
}
