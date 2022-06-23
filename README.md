# spot_micro_project
- raspberry pi 4B
- [Adafruit PCA9685](https://www.amazon.com/PCA9685/s?k=PCA9685)
- [DM-CLS400MD servomotor](https://www.devicemart.co.kr/goods/view?no=1324869)
- Body parts original model of [KDY0523](https://www.thingiverse.com/thing:3445283)
---
## steps
- clone this repository(already done)
- on raspberry pi terminal --> cd /home/minjun/motorProject/spot_micro_project/
- sudo sh requirements.sh
- cd /home/minjun/motorProject/spot_micro_project/main
- python3 returnInitial.py (initial position)
- code ./ (to modify with vscode)
---
## To Do...
- Rebuild Hardware (~ 06.12)
- Walk!(~ 06.12)
- other features like battery, LCD, etc (~ 07.03)
 --> individual division required before minjun nonsan...
- 07.07 ~ 07.28 minjun gone. Best regards:) 
---
## Hardware Plot
- electronics
![모식도](https://user-images.githubusercontent.com/68832065/172523955-014323d6-6b71-4081-909f-5676dc2463ff.jpg)
![KakaoTalk_20220622_150137653](https://user-images.githubusercontent.com/68832065/174955132-6d568d03-b8f3-4683-9bd5-18b6a60a6215.jpg)

- body
![KakaoTalk_20220608_121749178](https://user-images.githubusercontent.com/68832065/172524383-22f68d02-c0e9-4a5e-ae85-4bd4263f74de.jpg)

---
### movements
- sit

https://user-images.githubusercontent.com/68832065/173238778-4bf73b0d-ec79-4491-acd1-aca15e7adf5e.mp4

---
### for contributors
- clone that branch
- make changes

```bash
git checkout "branch name"
---------make changes----------
git add .
git commit -m "message"
git push 
```

- then redirect to reposity on chrome, make a pull request

**PLEASE DO NOT PUSH DIRECTLY TO MAIN**

---
### reference
- https://gitlab.com/public-open-source/spotmicroai
- https://learn.adafruit.com/16-channel-pwm-servo-driver?view=all
- https://www.thingiverse.com/thing:3445283
- https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup
- https://github.com/jordan-johnston271/yolov5-on-rpi4-2020
