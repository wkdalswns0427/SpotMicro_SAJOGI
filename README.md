# spot_micro_project
- raspberry pi 4B
- Adafruit PCA9685 with MG996R tower servo

### for we might need multiple PCA9685s notice the method of modifying I2C address
![Screenshot from 2022-05-16 09-21-08](https://user-images.githubusercontent.com/68832065/168500993-ffd28d3a-40e2-41e7-b420-a377f8bbf43d.png)

! issue : 잘 되던 8서보 제어가 갑자기 안됨. 전압 부족 추정되나 심적으로 는 그게 아닌거같음. 확인 요망
 코드 구동은 @dn0908이 할 줄 아니 물어볼 것

--> 확인 결과 드라이버에 capacitor가 없어서 잔류 전류 떄문에 오동작 하는 것으로 보임! 구형 드라이버로 하니까 잘 되네 구디굳:)
 
---
