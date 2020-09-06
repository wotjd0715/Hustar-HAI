## HAI-RC카를 이용한 자율주행

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
      ```  
      영상의 전처리를 위한 코드.
      영상을 읽어서 Edge Detction후
      각 프레임을 list에 넣어서 리턴한다.
      ```
   - learning.py 
      ```
      학습을 시키는 코드.
      데이터를 가져오고 학습 전 전처리를 하고
      모델을 만들고 학습 및 평가를 진행한다.
      ```
 ## Progress
 - [Week1- 프로젝트 사전 공부](/document/Week1.md)
 - [Week1- 프로젝트 사전 공부](/document/Week2.md) 
 - [Week1- 프로젝트 사전 공부](/document/Week3.md) 
 - [Week1- 프로젝트 사전 공부](/document/Week4.md) 
 - [Week1- 프로젝트 사전 공부](/document/Week5.md)  
 
 
 