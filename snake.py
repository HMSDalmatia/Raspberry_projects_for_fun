from machine import Pin, I2C
#import framebuf # First time managing buffor :D
import ssd1306
import time

# How Gemini sais:
# The ssd1306 library has a built-in function for drawing single pixels: pixel(x, y, color)

i2c = I2C(sda=Pin(0), scl=Pin(1))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
background_color = 0 # 1 white 0 black
pixel_color = 1 
snake_start_length = 5
# sample functions from gemini
def rysuj_przekatna():
    # 1. Wyczyść ekran
    oled.fill(0) # Wypełnia bufor kolorem 0 (czarny)

    # 2. Rysuj piksele
    for i in range(min(oled_width, oled_height)):
        oled.pixel(i, i, 1) # Rysuj biały piksel na (i, i)

    # 3. Wyślij bufor do wyświetlacza
    oled.show()
    
def animacja_chodzacy_piksel(czas_trwania=5):
    start_time = time.time()
    
    while (time.time() - start_time) < czas_trwania:
        for x in range(oled_width):
            # 1. Wyczyść poprzednią klatkę
            oled.fill(background_color) 

            # 2. Rysuj nowy piksel
            # Użyj np. 32 dla stałej wysokości
            oled.pixel(x, 32, pixel_color) 

            # 3. Wyślij nową klatkę do wyświetlacza
            oled.show()
            
            # 4. Krótka pauza, by zobaczyć ruch
            time.sleep(0.01) # 10 ms

# My function with snake
# arguments:
# 1. head_pixel_x, head_pixel_y are just coordinates of the snake's head
# 2. tail_pixel_x, tail_pixel_y are coordinates of the snake's tail end
# 3. break_x and break_y are coordinates of point where snake is being broke (like end of screen)
def snake(head_pixel_x, head_pixel_y, tail_pixel_x, tail_pixel_y, break_x, break_y, snake_length):
    len_head_break = round(((head_pixel_x - break_pixel_x)**2 + (head_pixel_y - break_pixel_y)**2)**0.5)
    len_break_tail = round(((break_pixel_x - tail_pixel_x)**2 + (break_pixel_y - tail_pixel_y)**2)**0.5)
    while len_head_tail + len_break_tail < snake_length:
        len_break_tail += 1
    # clearing screen
    for x in range(oled_width):
            oled.fill(background_color) 
animacja_chodzacy_piksel()
# rysuj_przekatna()




