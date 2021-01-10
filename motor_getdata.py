# -*- coding: utf-8 -*-

# 라즈베리파이 GPIO 패키지 
import RPi.GPIO as GPIO
import pygame
from time import sleep

pygame.init()

screen = pygame.display.set_mode((500,300))

# 모터 상태
STOP  = 0
FORWARD  = 1
BACKWORD = 2

# 모터 채널
CH1 = 0
CH2 = 1

# PIN 입출력 설정
OUTPUT = 1
INPUT = 0

# PIN 설정
HIGH = 1
LOW = 0

# 실제 핀 정의
#PWM PIN
ENA = 26  #37 pin
ENB = 0   #27 pin

#GPIO PIN
IN1 = 19  #37 pin
IN2 = 13  #35 pin
IN3 = 6   #31 pin
IN4 = 5   #29 pin

# 핀 설정 함수
def setPinConfig(EN, INA, INB):        
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    # 100khz 로 PWM 동작 시킴 
    pwm = GPIO.PWM(EN, 100) 
    # 우선 PWM 멈춤.   
    pwm.start(0) 
    return pwm

# 모터 제어 함수
def setMotorContorl(pwm, INA, INB, speed, stat):

    #모터 속도 제어 PWM
    pwm.ChangeDutyCycle(speed)  
    
    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
        
    #뒤로
    elif stat == BACKWORD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)
        
    #정지
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)

        
# 모터 제어함수 간단하게 사용하기 위해 한번더 래핑(감쌈)
def setMotor(ch, speed, stat):
    if ch == CH1:
        #pwmA는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
        #pwmB는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmB, IN3, IN4, speed, stat)
  

# GPIO 모드 설정 
GPIO.setmode(GPIO.BCM)
      
#모터 핀 설정
#핀 설정후 PWM 핸들 얻어옴 
pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

f = open("TestLog.txt", "w")


running = True;
data = 'start\n'
while running:
    for event in pygame.event.get():
        if event.type == pygame.K_q:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                setMotor(CH1, 30, BACKWORD)
                setMotor(CH2, 30, BACKWORD)
                print('STRAIGHT')
                data = 'STRAIGHT\n'
                #f.write('STRAIGHT\n')
            elif event.key == pygame.K_LEFT:
                setMotor(CH1, 0, BACKWORD)
                setMotor(CH2, 0, BACKWORD)
                setMotor(CH1, 30, BACKWORD)
                setMotor(CH2, 0, BACKWORD)
                print('LEFT')
                data = 'LEFT\n'
                #f.write('LEFT\n')
            elif event.key == pygame.K_RIGHT:
                setMotor(CH1, 0, BACKWORD)
                setMotor(CH2, 0, BACKWORD)
                setMotor(CH1, 0, BACKWORD)
                setMotor(CH2, 30, BACKWORD)
                print('RIGHT')
                data = 'RIGHT\n'
                #f.write('RIGHT\n')
            elif event.key == pygame.K_DOWN:
                setMotor(CH1, 0, BACKWORD)
                setMotor(CH2, 0, BACKWORD)
                print('STOP')
                data = 'STOP\n'
                #f.write('STOP\n')
    f.write(data)
    sleep(0.05)
        
    """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        print('STRAIGHT')
        keys = pygame.K_p
    elif keys[pygame.K_LEFT]:
        print('LEFT')
        keys = pygame.K_p
    elif keys[pygame.K_RIGHT]:
        print('RIGHT')
        keys = pygame.K_p
    """
            
f.close()
pygame.quit()

#제어 시작
'''
m_speed=0
while(True):
# 앞으로 80프로 속도로
    get = input("")
    check = 1
    if get == 1:
        setMotor(CH1, 0, BACKWORD)
        setMotor(CH2, 100, BACKWORD)
#5초 대기
        sleep(1)
        setMotor(CH1, 80, STOP)
        setMotor(CH2, 80, STOP)
    
    if get == 2:
        setMotor(CH1, 100, BACKWORD)
        setMotor(CH2, 100, BACKWORD)
#5초 대기
        sleep(1)
        setMotor(CH1, 80, STOP)
        setMotor(CH2, 80, STOP)
    
    if get == 3:
        setMotor(CH1, 100, BACKWORD)
        setMotor(CH2, 0, BACKWORD)
#5초 대기
        sleep(1)
        setMotor(CH1, 80, STOP)
        setMotor(CH2, 80, STOP)
"""
# 뒤로 40프로 속도로
setMotor(CH1, 40, BACKWORD)
setMotor(CH2, 40, BACKWORD)
sleep(5)

# 뒤로 100프로 속도로
setMotor(CH1, 100, BACKWORD)
setMotor(CH2, 100, BACKWORD)
sleep(5)
"""
#정지 
   

# 종료
GPIO.cleanup()
'''