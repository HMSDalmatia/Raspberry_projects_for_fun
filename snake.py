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
snake_length = 5
head_x = 8
head_y = 5
tail_x = 2
tail_y = 5
break_x = False
break_y = False
# sample function from gemini for good start (use it if You want but it is in Polish. English
# is being used later in my code (not gemini's ;D )
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
    
    start_time = time.time()
    while (time.time() - start_time) < czas_trwania:
        for x in range(oled_width,0, -1):
            # 1. Wyczyść poprzednią klatkę
            oled.fill(background_color) 

            # 2. Rysuj nowy piksel
            # Użyj np. 32 dla stałej wysokości
            oled.pixel(x, 32, pixel_color) 

            # 3. Wyślij nową klatkę do wyświetlacza
            oled.show()
            
            # 4. Krótka pauza, by zobaczyć ruch
            time.sleep(0.01) # 10 ms

# My functions with snake

# if snake is moving upwards y is changing, so, you write changing='y' and
# start and stop are coordinates of y
def drowning(change_start, change_stop, not_change, changing):
    if change_start - change_stop < 0:
        step = 1
    else:
        step = -1
    if changing == 'y':
        for y in range(change_start, change_stop, step):
            oled.pixel(not_change, y, pixel_color)
    elif changing == "x":
        for x in range(change_start, change_stop, step):
            oled.pixel(x, not_change, pixel_color)


def snake(head_pixel_x, head_pixel_y,  changing, length, tail_pixel_x, tail_pixel_y, is_breaking = False, breaking = False):
    if changing == 'x':
        drowning(tail_pixel_x, head_pixel_x, head_pixel_y, 'x')
    elif changing == 'y':
        drowning(tail_pixel_y, head_pixel_y, head_pixel_x, 'y')
    


while True:
    oled.fill(background_color)
    snake(head_x, head_y, 'x', snake_length, tail_x, tail_y)
    oled.show()
    head_x += 1
    tail_x += 1
    time.sleep(0.1)
    #animacja_chodzacy_piksel()
# rysuj_przekatna()




