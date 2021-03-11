#!/usr/bin/env python
import rospy

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

    path.poses.append(_pose_stamp(-0.0, -2, 4.712))
    # path.poses.append(_pose_stamp(-1.2, 1, 4.712))
    # path.poses.append(_pose_stamp(-1.4, 1, 4.712))
    # path.poses.append(_pose_stamp(-1.6, 1, 4.712))
    # path.poses.append(_pose_stamp(-1.8, 1, 4.712))
    # path.poses.append(_pose_stamp(-2.0, 1, 4.712))
    # path.poses.append(_pose_stamp(-2.2, 1, 4.712))
    # path.poses.append(_pose_stamp(-2.4, 1, 4.712))
    # path.poses.append(_pose_stamp(-2.6, 1, 4.712))
    # path.poses.append(_pose_stamp(-2.8, 1, 4.712))
    path.poses.append(_pose_stamp(-1.0, -2, 4.712))
    path.poses.append(_pose_stamp(-2.0, -2, 4.712))


    while not rospy.is_shutdown():
        pub.publish(path)
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
    try:
        publisher()
    except rospy:

        pass



    # p = PoseStamped()
    # s = PoseStamped()
    # a = PoseStamped()
    # b = PoseStamped()
    # c = PoseStamped()

    # p.header.frame_id = "map"
    # p.header.stamp = rospy.Time.now()
    # p.pose.position.x = -1
    # p.pose.position.y = 1
    # p.pose.position.z = 0
    # p.pose.orientation.x = 0.0
    # p.pose.orientation.y = 0.0
    # p.pose.orientation.z = 0.0
    # p.pose.orientation.w = 4.712

    # s.header.frame_id = "map"
    # s.header.stamp = rospy.Time.now()
    # s.pose.position.x = -1.2
    # s.pose.position.y = 1
    # s.pose.position.z = 0
    # s.pose.orientation.x = 0.0
    # s.pose.orientation.y = 0.0
    # s.pose.orientation.z = 0.0
    # s.pose.orientation.w = 4.712

    # a.header.frame_id = "map"
    # a.header.stamp = rospy.Time.now()
    # a.pose.position.x = -1.5
    # a.pose.position.y = 1
    # a.pose.position.z = 0
    # a.pose.orientation.x = 0.0
    # a.pose.orientation.y = 0.0
    # a.pose.orientation.z = 0.0
    # a.pose.orientation.w = 4.712

    # b.header.frame_id = "map"
    # b.header.stamp = rospy.Time.now()
    # b.pose.position.x = -1.8
    # b.pose.position.y = 1
    # b.pose.position.z = 0
    # b.pose.orientation.x = 0.0
    # b.pose.orientation.y = 0.0
    # b.pose.orientation.z = 0.0
    # b.pose.orientation.w = 4.712

    # c.header.frame_id = "map"
    # c.header.stamp = rospy.Time.now()
    # c.pose.position.x = -2
    # c.pose.position.y = 1
    # c.pose.position.z = 0
    # c.pose.orientation.x = 0.0
    # c.pose.orientation.y = 0.0
    # c.pose.orientation.z = 0.0
    # c.pose.orientation.w = 4.712 # 6.28


    # path.poses.append(p)
    # path.poses.append(s)
    # path.poses.append(a)
    # path.poses.append(b)
    # path.poses.append(c)