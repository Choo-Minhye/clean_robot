#!/usr/bin/env python
import rospy

from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, PoseArray

def publisher():

    pub = rospy.Publisher('/path_planning_node/cleaning_plan_nodehandle/cleaning_path', Path, queue_size=1)
    rospy.init_node('pose_publisher', anonymous=True)
    rate = rospy.Rate(10) # Hz
    p = PoseStamped()
    s = PoseStamped()
    a = PoseStamped()
    b = PoseStamped()
    c = PoseStamped()


    path = Path()

    path.header.frame_id = "map"
    path.header.stamp = rospy.Time.now()

    p.header.frame_id = "map"
    p.header.stamp = rospy.Time.now()
    p.pose.position.x = -1
    p.pose.position.y = 1
    p.pose.position.z = 0
    p.pose.orientation.x = 0.0
    p.pose.orientation.y = 0.0
    p.pose.orientation.z = 0.0
    p.pose.orientation.w = 4.712

    s.header.frame_id = "map"
    s.header.stamp = rospy.Time.now()
    s.pose.position.x = -2
    s.pose.position.y = 1
    s.pose.position.z = 0
    s.pose.orientation.x = 0.0
    s.pose.orientation.y = 0.0
    s.pose.orientation.z = 0.0
    s.pose.orientation.w = 4.712


    a.header.frame_id = "map"
    a.header.stamp = rospy.Time.now()
    a.pose.position.x = -3
    a.pose.position.y = 1
    a.pose.position.z = 0
    a.pose.orientation.x = 0.0
    a.pose.orientation.y = 0.0
    a.pose.orientation.z = 0.0
    a.pose.orientation.w = 4.712

    b.header.frame_id = "map"
    b.header.stamp = rospy.Time.now()
    b.pose.position.x = -4
    b.pose.position.y = 1
    b.pose.position.z = 0
    b.pose.orientation.x = 0.0
    b.pose.orientation.y = 0.0
    b.pose.orientation.z = 0.0
    b.pose.orientation.w = 4.712

    c.header.frame_id = "map"
    c.header.stamp = rospy.Time.now()
    c.pose.position.x = -4
    c.pose.position.y = 2
    c.pose.position.z = 0
    c.pose.orientation.x = 0.0
    c.pose.orientation.y = 0.0
    c.pose.orientation.z = 0.0
    c.pose.orientation.w = 6.28


    path.poses.append(p)
    path.poses.append(s)
    path.poses.append(a)
    path.poses.append(b)
    path.poses.append(c)

    while not rospy.is_shutdown():
        pub.publish(path)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy:

        pass
