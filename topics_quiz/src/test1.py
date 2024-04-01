#!/usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    dist = msg.ranges[0]
    print(dist)
    if dist <0.4 :
        turn.linear.x = 0
        turn.angular.z = 0
        pub.publish(turn)
        time.sleep(0.5)

        turn.linear.x = 0.1
        turn.angular.z = 1.57
        pub.publish(turn)
        rospy.sleep(0.25)

        turn.linear.x = 0
        turn.angular.z = 0
        pub.publish(turn)
    turn.linear.x = 0.25
    pub.publish(turn)

rospy.init_node('scan_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/scan', LaserScan, callback)

rate = rospy.Rate(2)
turn = Twist()

rospy.spin()

