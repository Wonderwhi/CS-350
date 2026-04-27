import RPi.GPIO as GPIO
import time

LED_PIN = 18
PWM_FREQ = 60

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


pwm18 = GPIO.PWM(LED_PIN, PWM_FREQ)

try:
    pwm18.start(0)

    while True:
        for duty in range(0,101, 5):
            pwm18.ChangeDutyCycle(duty)
            time.sleep(0.1)

        for  duty in range (100, -1, -5):
             pwm18.ChangeDutyCycle(duty)
             time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    pwm18.stop()
    GPIO.cleanup()

