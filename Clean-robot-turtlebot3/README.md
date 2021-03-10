
```bash
sudo apt install ros-${ROS_DISTRO}-turtlebot3 ros-${ROS_DISTRO}-navigation ros-${ROS_DISTRO}-dwa-local-planner ros-${ROS_DISTRO}-slam-karto
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
