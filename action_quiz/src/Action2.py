#!/usr/bin/env python

import rospy
import actionlib
from your_package_name.msg import Action2Action, Action2Feedback, Action2Result
from geometry_msgs.msg import PoseStamped

class Action2Server:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('action2', Action2Action, self.execute, False)
        self.server.start()
        self.pose_subscriber = rospy.Subscriber('/pose_topic', PoseStamped, self.pose_callback)
        self.current_orientation_x = 0.0

    def pose_callback(self, msg):
        self.current_orientation_x = msg.pose.orientation.x

    def execute(self, goal):
        rate = rospy.Rate(1) # 1 Hz
        orientations = []
        start_time = rospy.Time.now()

        while (rospy.Time.now() - start_time).to_sec() < goal.duration:
            if self.server.is_preempt_requested():
                self.server.set_preempted()
                break
            feedback = Action2Feedback()
            feedback.orientation_x = self.current_orientation_x
            self.server.publish_feedback(feedback)
            orientations.append(self.current_orientation_x)
            rate.sleep()

        result = Action2Result()
        result.orientations = orientations
        self.server.set_succeeded(result)

if __name__ == '__main__':
    rospy.init_node('action2_server')
    server = Action2Server()
    rospy.spin()
