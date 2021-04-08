#! /usr/bin/env python
import rospy
from my_summit_localization.srv import MyServiceMessage, MyServiceMessageResponse
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseWithCovarianceStamped
from send_coordinates_action_client import SendGoal
import actionlib
import time
import os
import rosparam

class GetGoal:
    def __init__(self):
        self.service = rospy.Service('/get_coordinates', MyServiceMessage , self.srv_callback)

    def srv_callback(self, request):

        label = request.label
        response = MyServiceMessageResponse()
  
        os.chdir("/home/user/catkin_ws/src/my_summit_localization/spots")
        spots = rosparam.load_file("spots.yaml")

        for params, name in spots:
            for key, value in params.items():
                if key == request.label:
                    rosparam.upload_params(name, params) 

        send_coordinates = SendGoal(request.label)

        response.navigation_successfull = True
        response.message = "Goal Reached"

        return response

if __name__ == "__main__":
    rospy.init_node('get_coordinates_node')
    get_coordinates_object = GetGoal()
    print("\nService Started\n")
    rospy.spin() 