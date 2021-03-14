/*
This code is used to plan the trajectory of the robot  
*/

#include <ros/ros.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "nav_msgs/Odometry.h"
#include "nav_msgs/Path.h"
#include "geometry_msgs/PoseStamped.h"
#include <tf/transform_listener.h>
#include <iostream>
#include <fstream>

using namespace std;
using namespace tf;

float x_current;
float y_current;

float normeNextGoal;

class quaternion_ros
{
public:
  float w;
  float x;
  float y;
  float z;

  quaternion_ros();

  void toQuaternion(float pitch, float roll, float yaw);
};

void quaternion_ros::toQuaternion(float pitch, float roll, float yaw)
{

  float cy = cos(yaw * 0.5);
  float sy = sin(yaw * 0.5);
  float cr = cos(roll * 0.5);
  float sr = sin(roll * 0.5);
  float cp = cos(pitch * 0.5);
  float sp = sin(pitch * 0.5);

  w = cy * cr * cp + sy * sr * sp;
  x = cy * sr * cp - sy * cr * sp;
  y = cy * cr * sp + sy * sr * cp;
  z = sy * cr * cp - cy * sr * sp;
}

quaternion_ros::quaternion_ros()
{
  w = 1;
  x = 0;
  y = 0;
  z = 0;
}

class Path_planned
{
public:
  struct Goal
  {
    float x;
    float y;
    float w;
    float z;
    bool visited;
  };

  vector<Goal> Path;

  Path_planned();
  // Path_planned(float x, float y, bool visited);
  void addGoal(float X, float Y, float W, float Z,bool visit);
};

Path_planned::Path_planned()
{
}

// Path_planned(float x, float y, bool visited)

void Path_planned::addGoal(float X, float Y, float W, float Z, bool visit)
{
  Path_planned::Goal newGoal;
  newGoal.x = X;
  newGoal.y = Y;
  newGoal.w = W;
  newGoal.z = Z;

  newGoal.visited = visit;
  Path.push_back(newGoal);
}

Path_planned planned_path;
nav_msgs::Path passed_path;
ros::Publisher pub_passed_path;
void pose_callback(const nav_msgs::Odometry &poses)
{ //현재 로봇 위치와 이전 목표 지점 사이의 거리를 계산하고 새 화면 스윙 지점을 보낼지 여부를 결정하는 데 사용되는 주행 콜백 함수
  x_current = poses.pose.pose.position.x;
  y_current = poses.pose.pose.position.y;

  passed_path.header = poses.header;
  geometry_msgs::PoseStamped p;
  p.header = poses.header;
  p.pose = poses.pose.pose;
  passed_path.poses.emplace_back(p);
  pub_passed_path.publish(passed_path);
}

int taille_last_path = 0;
bool new_path = false;

// 계획된 경로를 수락하는 곳!
void path_callback(const nav_msgs::Path &path)
{
  //rviz 표시의 편의를 위해 경로는 항상 전송되지만 여기서는 한 번만 수락하고 계획된 경로가 변경되면 다시 로드된다!
  if ((planned_path.Path.size() == 0) || (path.poses.size() != taille_last_path))
  {
    planned_path.Path.clear();
    new_path = true;
    for (int i = 0; i < path.poses.size(); i++)
    {
      planned_path.addGoal(path.poses[i].pose.position.x, path.poses[i].pose.position.y, path.poses[i].pose.orientation.w, path.poses[i].pose.orientation.z, false);


      cout << path.poses[i].pose.position.x << " " << path.poses[i].pose.position.y << endl;
    }
    cout << "Recv path size:" << path.poses.size() << endl;
    taille_last_path = path.poses.size();
  }

}

int main(int argc, char *argv[])
{
  srand(time(0));
  ros::init(argc, argv, "next_goal");
  ros::NodeHandle next_goal;
  ros::Subscriber sub1 = next_goal.subscribe("/odom", 1000, pose_callback);
  ros::Subscriber sub2 = next_goal.subscribe("/path_planning_node/cleaning_plan_nodehandle/cleaning_path", 1000, path_callback);

  ros::Publisher pub1 = next_goal.advertise<geometry_msgs::PoseStamped>("/move_base_simple/goal", 1000);
  pub_passed_path = next_goal.advertise<nav_msgs::Path>("/clean_robot/passed_path", 1000);

  ros::Rate loop_rate(10);

  geometry_msgs::PoseStamped goal_msgs;
  int count = 0;
  double angle;
  bool goal_reached = false;
  // 다음 포인트 값 얻기 위한 tolerance_ goal 설정 
  if (!next_goal.getParam("/NextGoal/tolerance_goal", normeNextGoal))
  {
    ROS_ERROR("Please set your tolerance_goal");
    return 0;
  }
  ROS_INFO("tolerance_goal=%f", normeNextGoal);

  while (ros::ok())
  {
    ros::spinOnce();
    if (new_path)
    {
      // planned_path.Path.clear();
      count = 0;
      new_path = false;
      goal_reached = false;

    }
    //현재 처리 된 포인트
    cout << " count : " << count << endl;
    if (!planned_path.Path.empty())
    { 
      //도착
      if (sqrt(pow(x_current - planned_path.Path[count].x, 2) + pow(y_current - planned_path.Path[count].y, 2)) <= normeNextGoal)
      {
        count++;
        goal_reached = false;
        cout << "arrived" <<endl;
      }
      if (goal_reached == false)
      {
        goal_msgs.header.frame_id = "odom";
        goal_msgs.header.stamp = ros::Time::now();
        goal_msgs.pose.position.x = planned_path.Path[count].x;
        goal_msgs.pose.position.y = planned_path.Path[count].y;
        goal_msgs.pose.position.z = 0;
        if (count < planned_path.Path.size())
        {
          angle = atan2(planned_path.Path[count + 1].y - planned_path.Path[count].y, planned_path.Path[count + 1].x - planned_path.Path[count].x);
        }
        else
        {
          angle = atan2(planned_path.Path[0].y - planned_path.Path[count].y, planned_path.Path[0].x - planned_path.Path[count].x);
        }
        cout<< "angle : "  << angle << endl;
        quaternion_ros q;
        q.toQuaternion(0, 0, float(angle));
        goal_msgs.pose.orientation.w = planned_path.Path[count].w;
        goal_msgs.pose.orientation.x = q.x;
        goal_msgs.pose.orientation.y = q.y;
        goal_msgs.pose.orientation.z = planned_path.Path[count].z;

        cout << " NEW GOAL " << endl;
        cout << " x = " << planned_path.Path[count].x << " y = " << planned_path.Path[count].y << endl;

        goal_reached = true;
        pub1.publish(goal_msgs);
      
      }
      if(count == planned_path.Path.size() && goal_reached == true){
        count = 0;
        
        goal_msgs.pose.position.x = x_current;
        goal_msgs.pose.position.y = y_current;
        planned_path.Path.clear();

        pub1.publish(goal_msgs);

        // if (planned_path.Path.empty()){
        //   cout << "also empty" << endl;
        // }

      }
      


      cout << x_current << " " << y_current << endl;
      cout << planned_path.Path[count].x << " " << planned_path.Path[count].y << endl;
      // cout << " DISTANCE : " << sqrt((x_current - planned_path.Path[count].x) * (x_current - planned_path.Path[count].x) + (y_current - planned_path.Path[count].y) * (y_current - planned_path.Path[count].y)) << endl;
    }

    else {
      count = 0;
    }

    loop_rate.sleep();
  }

  return 0;
}