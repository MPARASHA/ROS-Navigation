#! /usr/bin/env python

import rospy
import sys
from std_srvs.srv import Empty, EmptyRequest

# Initialise a ROS node with the name service_client
rospy.init_node('initialize_particles_client')
# Wait for the service client /trajectory_by_name to be running
rospy.wait_for_service('/global_localization')
# Create the connection to the service
traj_by_name_service = rospy.ServiceProxy('/global_localization', Empty)
# Create an object of type TrajByNameRequest 
traj_by_name_object = EmptyRequest()
# Fill the variable traj_name of this object with the desired value

# Send through the connection the name of the trajectory to be executed by the robot
traj_by_name_service(traj_by_name_object)
# Print the result given by the service called

