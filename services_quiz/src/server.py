#! /usr/bin/env python
import rospy
from datetime import datetime, timedelta
from services_pkg.srv import ms1, ms1Response
from geometry_msgs.msg import Twist

def my_callback(request):
    print("My_callback has been called")
#    the service Response class, in this c
    dir = 0
    if request.directie =="dreapta" :
        dir = 1
    else:
        dir = -1
    start_time = rospy.get_time()
    turn = Twist()
    Duration = request.durata
    while start_time + Duration > rospy.get_time():
        turn.linear.x = 0.1
        turn.angular.z = 0.7* dir
        pub.publish(turn)

    turn.linear.x = 0.0
    turn.angular.z = 0.0
    pub.publish(turn)

    response = ms1Response()
    response.succes = True
    return response

rospy.init_node('service_server')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
r = rospy.Rate(1)

my_service = rospy.Service('/move_sevice_quiz', ms1 , my_callback)
rospy.spin()