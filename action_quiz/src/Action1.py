#!/usr/bin/env python

import rospy
import actionlib
from geometry_msgs.msg import Twist
from action_quiz.msg import Action2Action, Action2Goal


def rotate_robot():
    # Publisher to send commands to the robot's wheels
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    # Give some time to establish the connection
    rospy.sleep(1)

    # Twist message to rotate the robot
    twist = Twist()
    twist.angular.z = 0.5  # Positive for left rotation, adjust the value based on the robot's capability

    # Duration of rotation
    rotation_time = rospy.Duration(5)  # Rotate for 5 seconds
    start_time = rospy.Time.now()

    # Send the command for the duration
    while rospy.Time.now() - start_time < rotation_time:
        pub.publish(twist)
        rospy.sleep(0.1)

    # Stop the robot after rotation
    twist.angular.z = 0
    pub.publish(twist)


def action2_client(duration):
    # Creates the SimpleActionClient, passing the type of the action to the constructor.
    client = actionlib.SimpleActionClient('action2', Action2Action)

    # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = Action2Goal(duration=duration)

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A Action2Result


if __name__ == '__main__':
    rospy.init_node('action2_client')

    # Rotate the robot first
    rotate_robot()

    # Then call the Action2 with a duration of 10 seconds
    result = action2_client(10)
    print("Action completed. Received orientations:", result.orientations)
