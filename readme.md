## HAI-RC카를 이용한 자율주행

### Members
- [박재성](https://github.com/wotjd0715)
- [권현수](https://github.com/KwonHyeonSu)
- [이진우](https://github.com/tgs04013)
- [이상목](https://github.com/SNMHZ)
- [양영우](https://github.com/YangYoungwoo)
- [윤동준](https://github.com/yundj4408)

### Project 
RC카가 자체 제작한 트랙에서 카메라만 이용하여 라인을 따라 자율 주행 하는 것을 목표로 한다.

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
   - [imgprocess.py](/imgprocess.py)
      ```  
      영상의 전처리를 위한 코드.
      영상을 읽어서 Edge Detction후
      각 프레임을 list에 넣어서 리턴한다.
      ```
   - [learning.py](/learning.py)
      ```
      학습을 시키는 코드.
      데이터를 가져오고 학습 전 전처리를 하고
      모델을 만들고 학습 및 평가를 진행한다.
      ```
 ## Progress
 - [Week1- 프로젝트 사전 공부](/document/Week1.md)
 - [Week2- Line Detecting](/document/Week2.md) 
 - [Week3- Hardware Design](/document/Week3.md) 
 - [Week4- 자율주행 Desgin & Test](/document/Week4.md) 
 - [Week5- Project Feedback](/document/Week5.md)  
 
 <br><br>

 --------

Hustar ICT 2020 소모임<br>
Hustar AI, HAI