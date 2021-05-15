#include <Wire.h>
#include "RTClib.h"

char daysOfTheWeek[7][12] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

#define pinRed 13
#define pinYellow 12
#define pinGreen 11
#define pinRele 10
#define pino_sinal_analogico A3
int valor_analogico;
bool solo_seco = false;
int intervalo = 0;

RTC_DS1307 rtc;

void setup() {
  Serial.begin(9600);
  //SET LIGTH START POINT
  pinMode(pinRed, OUTPUT);
  pinMode(pinYellow, OUTPUT);
  pinMode(pinGreen, OUTPUT);
  digitalWrite(pinRed, LOW); 
  digitalWrite(pinYellow, LOW); 
  digitalWrite(pinGreen, LOW); 

  //SET RELE START POINT
  pinMode(pinRele, OUTPUT);
  digitalWrite(pinRele, HIGH);
  
  //SET SENSOR DE UMIDADE
  pinMode(pino_sinal_analogico, INPUT);

  //SET RTC
  if (! rtc.begin()) {
    Serial.println("Não achei o RTC");
    while (1);
  }else{
    Serial.println("Achei o RTC");
  }
  //rtc.adjust(DateTime(2020, 05, 27, 12, 48, 00));
  if (! rtc.isrunning()) {
    Serial.println("RTC não está rodando!");
    // following line sets the RTC to the date & time this sketch was compiled
    //rtc.adjust(DateTime(2020, 05, 27, 06, 39, 00));
    //rtc.adjust(DateTime(2020, 05, 27, 12, 47, 00));
  }else{
    Serial.println("RTC está rodando!");
  }
  
}

void loop() {
  DateTime now = rtc.now();
  valor_analogico = analogRead(pino_sinal_analogico);

  //Mostra o valor da porta analogica no serial monitor
  Serial.print("Porta analogica: ");
  Serial.println(valor_analogico);
  if (valor_analogico > 0 && valor_analogico <= 340)
  {
    //SOLO ÚMIDO
    digitalWrite(pinGreen, HIGH);
    digitalWrite(pinRed, LOW); 
    digitalWrite(pinYellow, LOW); 
    solo_seco = false;
    intervalo = 0;
  }
 
  //Solo com umidade moderada, acende led amarelo
  if (valor_analogico > 340 && valor_analogico <= 681)
  {
    //UMIDADE MODERADA
    digitalWrite(pinYellow, HIGH);
    digitalWrite(pinRed, LOW); 
    digitalWrite(pinGreen, LOW);
    solo_seco = true;
    intervalo = 20;
  }
 
  //Solo seco, acende led vermelho
  if (valor_analogico > 681 && valor_analogico < 1024)
  {
    //SOLO SECO
    digitalWrite(pinRed, HIGH);
    digitalWrite(pinYellow, LOW); 
    digitalWrite(pinGreen, LOW);
    solo_seco = true;
    intervalo = 40;
  }

  if(solo_seco && now.hour() == 7 && now.minute() == 0){
    digitalWrite(pinRele, LOW); 
  }

  
  if(now.hour() == 7 && now.minute() == intervalo){
    digitalWrite(pinRele, HIGH); 
  }
  Serial.print("Data: "); //IMPRIME O TEXTO NO MONITOR SERIAL
  Serial.print(now.day(), DEC); //IMPRIME NO MONITOR SERIAL O DIA
  Serial.print('/'); //IMPRIME O CARACTERE NO MONITOR SERIAL
  Serial.print(now.month(), DEC); //IMPRIME NO MONITOR SERIAL O MÊS
  Serial.print('/'); //IMPRIME O CARACTERE NO MONITOR SERIAL
  Serial.print(now.year(), DEC); //IMPRIME NO MONITOR SERIAL O ANO
  Serial.print(" / Dia: "); //IMPRIME O TEXTO NA SERIAL
  Serial.print(daysOfTheWeek[now.dayOfTheWeek()]); //IMPRIME NO MONITOR SERIAL O DIA
  Serial.print(" / Horas: "); //IMPRIME O TEXTO NA SERIAL
  Serial.print(now.hour(), DEC); //IMPRIME NO MONITOR SERIAL A HORA
  Serial.print(':'); //IMPRIME O CARACTERE NO MONITOR SERIAL
  Serial.print(now.minute(), DEC); //IMPRIME NO MONITOR SERIAL OS MINUTOS
  Serial.print(':'); //IMPRIME O CARACTERE NO MONITOR SERIAL
  Serial.print(now.second(), DEC); //IMPRIME NO MONITOR SERIAL OS SEGUNDOS
  Serial.println(); //QUEBRA DE LINHA NA SERIAL
  delay(1000);
}
