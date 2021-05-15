#include <Wire.h> //INCLUSÃO DA BIBLIOTECA
#include "RTClib.h" //INCLUSÃO DA BIBLIOTECA
 
RTC_DS1307 rtc; //OBJETO DO TIPO RTC_DS1307
 
//DECLARAÇÃO DOS DIAS DA SEMANA
char daysOfTheWeek[7][12] = {"Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"};
 
void setup () {  
    Serial.begin(57600);  
    // following line sets the RTC to the date & time this sketch was compiled  
    rtc.begin(DateTime(F(__DATE__), F(__TIME__)));  
    // This line sets the RTC with an explicit date & time, for example to set  
    // January 21, 2014 at 3am you would call:  
    // rtc.adjust(DateTime(2014, 1, 21, 3, 0, 0));  
}  
void loop () {

}
