#! /usr/bin/env python

import rospy
import sys
from nav_msgs.srv import GetMap, GetMapRequest

# Initialise a ROS node with the name service_client
rospy.init_node('map_service_client')
# Wait for the service client /trajectory_by_name to be running
rospy.wait_for_service('/static_map')
# Create the connection to the service
traj_by_name_service = rospy.ServiceProxy('/static_map', GetMap)
# Create an object of type TrajByNameRequest 
traj_by_name_object = GetMapRequest()
# Fill the variable traj_name of this object with the desired value

# Send through the connection the name of the trajectory to be executed by the robot
result = traj_by_name_service(traj_by_name_object)
# Print the result given by the service called
print (result.map.header)
