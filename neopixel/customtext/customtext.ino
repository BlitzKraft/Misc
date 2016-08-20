#include <Adafruit_NeoPixel.h>

#define PIN 6

Adafruit_NeoPixel strip = Adafruit_NeoPixel(40, PIN, NEO_GRB + NEO_KHZ800 );

uint32_t magenta = strip.Color(255, 0, 255);
uint32_t off = strip.Color(0, 0, 0);

int dtime = 400;

void setup() {
	strip.begin();
	strip.setBrightness(16);
	strip.show();
}

void loop() {
	int H[] = {0, 8, 16, 24, 32, 17, 18, 3, 11, 19, 27, 35};
	for(int j = 0; j < 7; j++) {
		for(int i = 0; i < sizeof(H); i++) {
			strip.setPixelColor(H[i] + j, magenta);
		}
		strip.show();
		delay(dtime);
		for(int i = 0; i < sizeof(H); i++) {
			strip.setPixelColor(H[i] + j, off);
		}
		strip.show();
		delay(100);
	}
	delay(dtime);
}
