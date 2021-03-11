### 다운로드
```bash
sudo apt install ros-melodic-turtlebot3 ros-melodic-navigation ros-melodic-dwa-local-planner ros-melodic-slam-karto
```
### 맵 그리고 동작
```bash
export TURTLEBOT3_MODEL=burger 
roslaunch clean_robot auto_slam.launch
```
### path point 실행
```bash
export TURTLEBOT3_MODEL=burger 
roslaunch clean_robot clean_work.launch
rosrun clean_robot pub_path.py
```
