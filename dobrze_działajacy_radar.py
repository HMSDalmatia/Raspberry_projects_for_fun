from machine import Pin
import utime

# Stałe
# Prędkość dźwięku w cm/us (mikrosekundach)
SOUND_SPEED_CM_PER_US = 0.0343

# Ustawienie pinów
echo = Pin(0, Pin.IN)
trig = Pin(1, Pin.OUT)

# wlasciwy pomiar
def get_distance():
    # Wyzwolenie impulsu
    trig.value(0)
    utime.sleep_us(2)
    trig.value(1)
    utime.sleep_us(10) # wynika ze specyfikacji czujnika
    trig.value(0)

    # Pomiar czasu sygnału
    timeout_us = 25000  # Dodano timeout dla bezpieczeństwa
    
    pulse_start = utime.ticks_us() # pobranie czasu przed wyjsciem impulsu (dla bezpieczenstwa)
    while echo.value() == 0 and utime.ticks_us() - pulse_start < timeout_us: # echo zmienia stan na wysoki jak pojdzie pierwszy sygnal
        pass
    start_time = utime.ticks_us() # Włączamy stoper w momencie, gdy pin echo przechodzi w stan wysoki (sygnał wyjściowy czujnika).

    while echo.value() == 1 and utime.ticks_us() - start_time < timeout_us: # tak dlugo az impuls nie wraca echo pozostaje w stanie wysokim
        pass
    end_time = utime.ticks_us() # zgarniecie czasu po powrocie

    # Obliczanie odległości
    time_elapsed = end_time - start_time
    distance_cm = (time_elapsed * SOUND_SPEED_CM_PER_US) / 2
    
    # Walidacja danych
    # Standardowy czujnik HC-SR04 działa w zakresie 2-400 cm
    if distance_cm > 400 or distance_cm < 2:
        return None  # Zwróć None, jeśli pomiar jest poza zakresem
    
    return distance_cm

# Główna pętla
while True:
    distance = get_distance()
    if distance is not None:
        print(f"Odległość od obiektu: {distance:.2f} cm")
    else:
        print("Pomiar poza zakresem lub błąd pomiaru.")
        
    utime.sleep_ms(250)