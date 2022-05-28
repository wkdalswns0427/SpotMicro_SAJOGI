#include <wiringPi.h>
#include <stdio.h>
#include <softPwm.h>
#define SERVO 18

int main(void){
    wiringPiSetupGpio();
    pinMode(SERVO, OUTPUT);

    while(1){
        printf("loop init");
        softPwmWrite(SERVO, 10);
        delay(500);
        softPwmWrite(SERVO, 20);
        delay(500);
        softPwmWrite(SERVO, 30);
        delay(500);
    }
    return 0;
}