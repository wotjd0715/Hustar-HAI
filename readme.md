## HAI-RC카를 이용한 자율주행

### INDEX
 1. [Members](https://github.com/wotjd0715/Hustar-HAI#Members)
 2. [Project](https://github.com/wotjd0715/Hustar-HAI#Project)
 3. [Project Detail](https://github.com/wotjd0715/Hustar-HAI#ProjectDetail)
 4. [Code](https://github.com/wotjd0715/Hustar-HAI#Code)
 5. [Progress](https://github.com/wotjd0715/Hustar-HAI#Progress)
 
 

### Members
- 박재성
- 권현수
- 이진우 
- 이상목
- 양영우
- 윤동준

### Project 
RC카가 직접 만든 바닥의 트랙에서 카메라를 이용한 라인 디텍팅을 통해 자율주행을 하는것을 목표로 한다.

### Project Detail
SW   
 - Camera & Line detecting (OpenCV Library 활용)
 - Determine Car Action Model (Tensorflow CNN - MNN)
 - Control RC car (Raspberrypi GPIO with Motor Drive)

HW
 - Motors for driving
 - USB camera module for get line image
 - Motor shield(L298N) for control motor
 - Raspberrypi for Input data

### Code
   - imgprocess.py
   - learning.py 
 ## Progress
 - [Week1- 프로젝트 사전 공부](/document/Week1.md) 
 
 ###Day2 - 프로젝트 사전 공부
 내용 - CodeIT에서 머신러닝의 기본적인 개념에 대해 공부 함 (CNN, MNN 등) 
   
 어려웠던점 - 자율주행의 원리 조차 몰랐으며 그로 인해 어떤걸 공부해야할지 몰라 어려움을 겪음   
 또한 CodeIT 만으로는 인공지능을 공부하기에는 부족였고 전반적인 기초 베이스 역시 부족하였다.    
 그로인해 자율주행을 어떻게 만들어야하는지 막막함을 느겼다.
 
 배운점 - 인공지능이 어떻게 학습하고 어떻게 동작하는지 전체적인 흐름을 배웠고 기본적인 Concept에 대해 알 수 있었다.   
 이미지 처리에 쓰이는 기본적인 CNN에 대한 개념과 가장 기본 형태의 MNN을 공부하였고 LaneNet, PathNet, YOLO 등을 공부 하였으나 
 실제로 사용하기에는 어려움이 있다고 판단하여 OpenCV를 이용하여 전처리후 CNN과 MNN을 이용한 모델을 구성하기로 하였다.
 
 