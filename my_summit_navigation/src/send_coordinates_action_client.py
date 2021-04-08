#! /usr/bin/env python

import rospy
from my_summit_localization.srv import MyServiceMessage, MyServiceMessageResponse
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseAction, MoveBaseResult, MoveBaseGoal
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseWithCovarianceStamped

import actionlib
from actionlib_msgs.msg import GoalStatus

import time
import os
import rosparam

class SendGoal:
    def __init__(self, label):

        self.label = label

        client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)

        goal = MoveBaseGoal()
        goalPose = Pose()

        rospy.on_shutdown(self.shutdownhook)

        # Set the Goal Coords
        goalPose.position.x = rosparam.get_param(self.label + '/position/x')
        goalPose.position.y = rosparam.get_param(self.label + '/position/y')
        goalPose.position.z = rosparam.get_param(self.label + '/position/z')

        # Set the Goal Orientation
        goalPose.orientation.x = rosparam.get_param(self.label + '/orientation/x')
        goalPose.orientation.y = rosparam.get_param(self.label + '/orientation/y')
        goalPose.orientation.z = rosparam.get_param(self.label + '/orientation/z')
        goalPose.orientation.w = rosparam.get_param(self.label + '/orientation/w')

        goal.target_pose.pose = goalPose

        goal.target_pose.header.frame_id = 'map'

        client.wait_for_server()
        client.send_goal(goal, feedback_cb = self.callback)
        client.wait_for_result()
        result=client.get_state()

        if result==3:
            self.shutdownhook()


    def shutdownhook(self):
        return

    def callback(self, data):
        return