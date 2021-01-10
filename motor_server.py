# -*- coding: utf-8 -*-

# 라즈베리파이 GPIO 패키지 
import RPi.GPIO as GPIO
from time import sleep
import socket

HOST = '192.168.43.218'
PORT = 65432

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


running = True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while running:
            data = conn.recv(1024)
            #conn.sendall(data)
            m_data=data.decode()
            print('*', end='')
            if m_data=='':
                print('void')
            else:
                m_int_data=int(data)
                print(m_int_data)
                if m_int_data == 999:
                    running = False
                elif m_int_data == 1: #UP
                    setMotor(CH1, 15, BACKWORD)
                    setMotor(CH2, 15, BACKWORD)
                elif m_int_data == 0: #LEFT
                    setMotor(CH1, 0, BACKWORD)
                    setMotor(CH2, 0, BACKWORD)
                    setMotor(CH1, 30, BACKWORD)
                    setMotor(CH2, 0, BACKWORD)
                elif m_int_data == 2: #RIGHT
                    setMotor(CH1, 0, BACKWORD)
                    setMotor(CH2, 0, BACKWORD)
                    setMotor(CH1, 0, BACKWORD)
                    setMotor(CH2, 30, BACKWORD)
                elif m_int_data == 5: #DOWN
                    setMotor(CH1, 0, BACKWORD)
                    setMotor(CH2, 0, BACKWORD)
    GPIO.cleanup()