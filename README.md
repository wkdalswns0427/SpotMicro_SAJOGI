# spot_micro_project
- raspberry pi 4B
- Adafruit PCA9685 with MG996R tower servo

## steps
- clone this repository(already done)
- on raspberry pi terminal --> cd /home/minjun/motorProject/spot_micro_project/main
- python3 returnInitial.py (initial position)
- code ./ (to modify with vscode)

### for we might need multiple PCA9685s notice the method of modifying I2C address
![Screenshot from 2022-05-16 09-21-08](https://user-images.githubusercontent.com/68832065/168500993-ffd28d3a-40e2-41e7-b420-a377f8bbf43d.png)

! issue : 잘 되던 8서보 제어가 갑자기 안됨. 전압 부족 추정되나 심적으로 는 그게 아닌거같음. 확인 요망
 코드 구동은 @dn0908이 할 줄 아니 물어볼 것

--> 확인 결과 드라이버에 capacitor가 없어서 잔류 전류 떄문에 오동작 하는 것으로 보임! 구형 드라이버로 하니까 잘 되네 구디굳:)

---
![캡처](https://user-images.githubusercontent.com/68832065/171987098-c1535424-1386-4429-a698-c221a35c64bc.JPG)


 ![KakaoTalk_20220603_173604001](https://user-images.githubusercontent.com/68832065/171987062-fc06ff3f-06b6-4646-a143-74abaa503e16.jpg)

---
### reference
- https://learn.adafruit.com/16-channel-pwm-servo-driver?view=all
- https://www.thingiverse.com/thing:3445283
