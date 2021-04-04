#!/usr/bin/env python
import rospy
# import time
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, PoseArray
from tf.transformations import *


def publisher():

    pub = rospy.Publisher('/path_planning_node/cleaning_plan_nodehandle/cleaning_path', Path, queue_size=1)
    rospy.init_node('pose_publisher', anonymous=True)
    rate = rospy.Rate(10) # Hz

    path = Path()

    path.header.frame_id = "map"
    path.header.stamp = rospy.Time.now()
    path.poses.append(_pose_stamp(0.0, 0.0, 0))
    path.poses.append(_pose_stamp(3.5, 0.0, 90))
    path.poses.append(_pose_stamp(4.5, 0.0, 60))
    path.poses.append(_pose_stamp(7.5, 0.0, 180))
  

    while not rospy.is_shutdown():
        connections = pub.get_num_connections()
        if connections > 0:
            pub.publish(path)
            break

        rate.sleep()


def _pose_stamp(x,y,_degree) :
    pose_stamp = PoseStamped()
    pose_stamp.header.frame_id = "map"
    pose_stamp.header.stamp = rospy.Time.now()
    pose_stamp.pose.position.x = x
    pose_stamp.pose.position.y = y
    pose_stamp.pose.position.z = 0
    pose_stamp.pose.orientation.x = 0.0
    pose_stamp.pose.orientation.y = 0.0
    pose_stamp.pose.orientation.z = radian_to_quat( math.radians(_degree))[2]
    pose_stamp.pose.orientation.w = radian_to_quat( math.radians(_degree))[3]
    
    return pose_stamp

def radian_to_quat(r) :
    q = quaternion_from_euler(0, 0, r)
    return q


if __name__ == '__main__':
    publisher()
    print("good")



#  move_base_flex/move_base/goal