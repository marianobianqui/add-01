from machine import Pin
import time
led = Pin(1,Pin.OUT)
pulsador = Pin(28,Pin.IN)
led2 = Pin(2,Pin.OUT)
pulsador2 = Pin(27,Pin.IN)
while 1:
 led.value(pulsador.value())
 if pulsador2.value() == 1:
  led2.value(not led2.value())
  time.sleep(.5)
