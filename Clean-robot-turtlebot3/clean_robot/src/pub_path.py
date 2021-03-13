#!/usr/bin/env python
import rospy

# import time
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, PoseArray

def publisher():

    pub = rospy.Publisher('/path_planning_node/cleaning_plan_nodehandle/cleaning_path', Path, queue_size=1)
    rospy.init_node('pose_publisher', anonymous=True)
    rate = rospy.Rate(10) # Hz

    path = Path()

    path.header.frame_id = "map"
    path.header.stamp = rospy.Time.now()
    path.poses.append(_pose_stamp(1.0, 0.5, 1.5708))
    path.poses.append(_pose_stamp(2.0, 0.5, 1.5708))
    path.poses.append(_pose_stamp(3.0, 0.5, 1.5708))
    
    # path.poses.append(_pose_stamp(0.0, 0.0, 6.28))
    # path.poses.append(_pose_stamp(1.0, 0.0, 6.28))
    # path.poses.append(_pose_stamp(2.0, 0.0, 6.28))

    # path.poses.append(_pose_stamp(0.0, 0.0, 0))
    # path.poses.append(_pose_stamp(6.0, 0.0, -0.523599))
    # path.poses.append(_pose_stamp(7.5, 2.0, -1.5708))
    # path.poses.append(_pose_stamp(7.5, 5.0, -1.5708))
    # path.poses.append(_pose_stamp(7.5, 8.0, -0.523599))
    # path.poses.append(_pose_stamp(8.5, 8.5, -0.785398))
    # path.poses.append(_pose_stamp(9.5, 9.0, -1.0472))
    # path.poses.append(_pose_stamp(10.3, 10.0, -1.0472))
    # path.poses.append(_pose_stamp(10.5, 11.0, -1.8326))
    # path.poses.append(_pose_stamp(10.0, 12.0, -3.14159))
    # path.poses.append(_pose_stamp(9.0, 12.0, -3.66519))
    # path.poses.append(_pose_stamp(7.5, 10.0, -4.36332))
    # path.poses.append(_pose_stamp(7.5, 10.0, -4.71239))
    # path.poses.append(_pose_stamp(7.5, 8.0, -4.71239))
    # path.poses.append(_pose_stamp(7.5, 5.0, -4.71239))
    # path.poses.append(_pose_stamp(7.5, 2.0, -4.88692))
    # path.poses.append(_pose_stamp(8.0, -4.5, -4.71239))
    # path.poses.append(_pose_stamp(8.0, -7.0, -4.71239))
    # path.poses.append(_pose_stamp(8.0, -10.0, -5.75959))
    # path.poses.append(_pose_stamp(11.0, -11.0, -0.785398))
    # path.poses.append(_pose_stamp(11.5, -10.0, -1.5708))
    # ###### EV turn ######
    # path.poses.append(_pose_stamp(11.5, -10.0, -3.1415))
    # path.poses.append(_pose_stamp(8.0, -10.0, -0.785398))
    # path.poses.append(_pose_stamp(8.0, -10.0, -1.5708))
    # path.poses.append(_pose_stamp(8.0, -7.0, -1.5708))
    # path.poses.append(_pose_stamp(8.0, -4.5, -1.8326))
    # path.poses.append(_pose_stamp(6.0, -0.5, -3.05433))
    # path.poses.append(_pose_stamp(0.0, 0.0, 0))

    while not rospy.is_shutdown():
        connections = pub.get_num_connections()
        if connections > 0:
            pub.publish(path)
            break

        rate.sleep()


def _pose_stamp(x,y,w) :
    pose_stamp = PoseStamped()

    pose_stamp.header.frame_id = "map"
    pose_stamp.header.stamp = rospy.Time.now()
    pose_stamp.pose.position.x = x
    pose_stamp.pose.position.y = y
    pose_stamp.pose.position.z = 0
    pose_stamp.pose.orientation.x = 0.0
    pose_stamp.pose.orientation.y = 0.0
    pose_stamp.pose.orientation.z = 0.0
    pose_stamp.pose.orientation.w = w
    
    return pose_stamp





if __name__ == '__main__':
    publisher()
    print("good")


