#!/usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    dist = msg.ranges[0]
    print(dist)


rospy.init_node('scan_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/scan', LaserScan, callback)

rate = rospy.Rate(2)
turn = Twist()

rospy.spin()

