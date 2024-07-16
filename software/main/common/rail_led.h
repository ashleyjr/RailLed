#ifndef INC_RAIL_LED_H
#define INC_RAIL_LED_H

#define OUTPUT_MODE  32
#define OUTPUT_SHDN1 33
#define OUTPUT_SHDN2 12
#define OUTPUT_SHDN3 13
#define OUTPUT_SHDN4 14
#define OUTPUT_SHDN5 16
#define OUTPUT_SHDN6 17
#define OUTPUT_SCLK  23
#define OUTPUT_BLANK 22
#define OUTPUT_XLAT  21
#define OUTPUT_SOUT  19
#define INPUT_SIN    18


#define NUM_ICS            1
#define NUM_LEDS_PER_IC    24
#define SHIFT_PER_IC_BITS  288
#define SHIFT_BITS         (SHIFT_PER_IC_BITS * NUM_ICS)
#define SHIFT_BYTES        (SHIFT_BITS / 8)


typedef uint16_t leds[NUM_LEDS_PER_IC];

#endif
