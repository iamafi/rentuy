
#include <avr/io.h>
#define F_CPU 16000000UL
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#include "_main.h"
#include "_buzzer.h"
#include "_adc.h"
#include "_eeprom.h"
#include "_init.h"
#include "_interrupt.h"
#include "_port.h"
#include "_timer2.h"
#include "_uart.h"
#include "_glcd.h"

#include <avr/pgmspace.h>

const unsigned char PROGMEM lookup[] = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ";

int main(void)
{
	unsigned char a;
	DDRB = 0xFF;
	
	init_devices();
	while (1){
		for (char i=0; i < 256; i++){
			a = pgm_read_byte(&lookup[i]);
			PORTB = ~(a - 0x30);
			_delay_ms(1000);
			lcd_clear();							// clear LCD
			ScreenBuffer_clear();					// clear screen buffer
			lcd_string(0,0,"U1910160 Ziyamova" );
			lcd_string(1,0,"Maftuna");
			lcd_string(2,0," ");
			lcd_string(3,0, "EEPROM Data");
			lcd_xy(4,0);
			lcd_char(a);
		}
	}
	return 0;
}
