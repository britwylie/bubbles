#include <Adafruit_NeoPixel.h>

// Which pin on the Arduino is connected to the NeoPixels?
// On a Trinket or Gemma we suggest changing this to 1:
#define LED_PIN    6
 
// How many NeoPixels are attached to the Arduino?
#define LED_COUNT 29
    
// Declare our NeoPixel strip object:
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
// Argument 1 = Number of pixels in NeoPixel strip
// Argument 2 = Arduino pin number (most are valid)
// Argument 3 = Pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
//   NEO_RGBW    Pixels are wired for RGBW bitstream (NeoPixel RGBW products)


void setup() {
  // put your setup code here, to run once:
  strip.begin();
  strip.setBrightness(64);
  strip.show();
}

void loop() {
  // put your main code here, to run repeatedly:
  chase(strip.Color(255, 0, 0));
  chase(strip.Color(0, 255, 0));
  chase(strip.Color(0, 0, 255));
}


static void chase(uint32_t c) {
  for(uint16_t i=0; i<strip.numPixels()+4; i++) {
    strip.setPixelColor(i , c);
    strip.setPixelColor(i-4, 0);
    strip.show();
    delay(70);
  }
}
