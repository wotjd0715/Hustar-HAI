 ### Week 2 - Line Detecting
 ### **내용** 
 동영상으로 찍은 트랙을 OpenCV에서 Canny와 Hough transform을 이용해 Line Detecting을 하였고
 실시간으로 카메라 모듈로부터 영상 받아오기위헤 MJPG Streamer, Cheese, 라즈베리파이 카메라 모듈을 사용해 보았다.  
 
 자율주행용 Track   
 ![image1](/document/images/image2.jpg)    
 
 OpenCV를 이용한 Line Detecting   
 ![image1](/document/images/image3.jpg)
 ![image1](/document/images/image4.jpg)  

 ### **어려웠던점**
  Line Detecting을 구현하는데 있어 시간이 오래 걸릴줄 알았지만 OpenCV라는 라이브러리를 이용하다보니 생긱보다 쉽게 Line Detecting을 
  할수 있었다. 하지만 실제로 Line을 검출할때 쓰이는 Hough Transform과 다른 개념을 이해하는데 어려움을 겪었다
 
 ### **배운점**  
 어떻게 구현해야 할까 막막했지만 OpenCV라는 라이브러리의 존재를 알게 되었고 YOLO 등 Python에서 제공하는 라이브러리의 다양성과 편리성에 대해
 알게되었다. 또 생각보다 같은 인터넷에 Open source code가 많아 이를 활용하여 코딩하는 방법을 배울 수 있었다.
 
 
 **박재성**   
 처음에는 자율주행을 하기 위해서는 어떤 기능들이 필요한지 고민하였다.
 그중 나온것이 차선인식이었지만 이것을 어떻게 해야하는지도 막막하게 느껴졌다. 여러가지 검색을 하면서 알아낸것이 OpenCV에서 제공하는 라이브러리를 사용하거나
 LaneNet, PathNet등을 활용하는 것이였다. 관련된 여러 논문들도 읽어 보면서 여러가지 방법을 써서 차선인식을 하고 싶었지만 우리가 성공할 수 있었던 것은 OpenCV뿐이였다..
 이마져도 검색을 통해 가져온 코드에서 이것저것 바꿔보며 어떤 역활을 하는지 알아보았고 또 거기에 사용된 수학적 개념(Hough Transform)들을 블로깅을 통해서 같이 공부해가면서
 프로젝트를 진행했다. 그래도 
 
 
 **양영우**   
 Colab에서 line detecting을 설계하기 전 MNIST를 이용하여 손글씨를 인식하는 법을 먼저 배운 뒤 line detecting을 시도하였다.   
 line detecting을 위해 이미지를 Blur를 처리한 후 Canny를 이용하여 모든 line을 찾은 뒤 관심 영역을 지정하고 허프 변환으로 line을 detecting하는 법을 배웠다.   
 허프 변환을 이용할 때 line을 완벽하게 받아오지 못하는 경우가 있어 Canny가 프로젝트에 더 맞는다고 생각할 수 있었다.   
 
