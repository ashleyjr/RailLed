/* BSD Socket API Example

   This example code is in the Public Domain (or CC0 licensed, at your option.)

   Unless required by applicable law or agreed to in writing, this
   software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
   CONDITIONS OF ANY KIND, either express or implied.
*/
#include <string.h>
#include <sys/param.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_wifi.h"
#include "esp_event.h"
#include "esp_log.h"
#include "nvs_flash.h"
#include "esp_netif.h"
#include "protocol_examples_common.h"

#include "lwip/err.h"
#include "lwip/sockets.h"
#include "lwip/sys.h"
#include <lwip/netdb.h>

#include "driver/gpio.h"

#include "../common/rail_led.h"

static const char *TAG = "main";

void app_main(void){
   gpio_config_t io_conf = {};

   // Create all output
   io_conf.intr_type = GPIO_INTR_DISABLE; 
   io_conf.mode = GPIO_MODE_OUTPUT;
   io_conf.pin_bit_mask =  
      ((uint64_t)1 << OUTPUT_MODE)| 
      ((uint64_t)1 << OUTPUT_SHDN1)|
      ((uint64_t)1 << OUTPUT_SHDN2)|
      ((uint64_t)1 << OUTPUT_SHDN3)|
      ((uint64_t)1 << OUTPUT_SHDN4)|
      ((uint64_t)1 << OUTPUT_SHDN5)|
      ((uint64_t)1 << OUTPUT_SHDN6)|
      ((uint64_t)1 << OUTPUT_SCLK)|
      ((uint64_t)1 << OUTPUT_BLANK)|
      ((uint64_t)1 << OUTPUT_XLAT)| 
      ((uint64_t)1 << OUTPUT_SOUT); 
   io_conf.pull_down_en = 0; 
   io_conf.pull_up_en = 1;
   gpio_config(&io_conf);
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_MODE, 0));
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_SHDN1, 0));
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_SHDN2, 0));
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_SHDN3, 0));
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_SHDN4, 0));
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_SHDN5, 0));
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_SHDN6, 0));
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_SCLK, 0));
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_BLANK, 0));
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_XLAT, 0));
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_SOUT, 0));

   // Create all output 
   io_conf.intr_type = GPIO_INTR_DISABLE; 
   io_conf.mode = GPIO_MODE_INPUT;
   io_conf.pin_bit_mask = ((uint64_t)1 << INPUT_SIN);
   gpio_config(&io_conf);



   
   ESP_LOGI(TAG, "Read as %d", gpio_get_level(INPUT_SIN));
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_XLAT, 1));
   ESP_LOGI(TAG, "Read as %d", gpio_get_level(INPUT_SIN));
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_SOUT, 1));
   ESP_LOGI(TAG, "Read as %d", gpio_get_level(INPUT_SIN)); 
   ESP_ERROR_CHECK(gpio_set_level(OUTPUT_SOUT, 0)); 
   ESP_LOGI(TAG, "Read as %d", gpio_get_level(INPUT_SIN)); 
}
