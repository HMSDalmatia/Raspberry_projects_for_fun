from machine import Pin, I2C
#import framebuf # First time managing buffor :D
import ssd1306
import time



i2c = I2C(sda=Pin(0), scl=Pin(1))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
background_color = 0 # 1 white 0 black
pixel_color = 1 
snake_length = 5
head_x = oled_width//2
head_y = oled_height//2
head_coordinates = [head_x, head_y]
snake = [head_coordinates]
direction = 'u'
for i in range(snake_length-1):
    snake.append([head_coordinates[0]-i-1, head_coordinates[1]])

def movement(sn, direct):
    if direct=='u': # up
        for i in range(len(sn)):
            sn[i][0] += 1
    elif direct=='l': # left
        for i in range(len(sn)):
            sn[i][1] -= 1
    elif direct=='r': # right
        for i in range(len(sn)):
            sn[i][1] += 1
    elif direct=='d': # up
        for i in range(len(sn)):
            sn[i][0] -= 1

def turn(direc):
    if direc == 'l' and direction == 'u': # left
        for i in range(len(snake)):
            snake[i][1] += 1
            movement(snake[:i+1], 'l')
            movement(snake[i+1:], 'u')
            print(snake)
            

while True:
    oled.fill(background_color)
    for i in range(len(snake)):
        oled.pixel(snake[i][0], snake[i][1], pixel_color)
    if snake[0][0] == 127 or snake[0][0] == 1:
        turn('l')
        direction = 'l'
        movement(snake, direction)
    elif snake[0][1] == 63 or snake [0][1] == 1:
        movement(snake, 'd')
    else:
        movement(snake, direction)
    oled.show()
    time.sleep(0.01)
