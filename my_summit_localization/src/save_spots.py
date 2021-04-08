#! /usr/bin/env python
import rospy
from my_summit_localization.srv import MyServiceMessage, MyServiceMessageResponse
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseWithCovarianceStamped
import time

class SaveSpots:
    def __init__(self):
        self.pose = PoseWithCovarianceStamped()
        self.spot_dict = {}
        self.service = rospy.Service("/record_spot", MyServiceMessage , self.srv_callback)
        self.sub_amcl_pose = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped , self.subscriber_callback)

    def subscriber_callback(self, msg):
        self.pose = msg

    def srv_callback(self, request):
        label = request.label
        response = MyServiceMessageResponse()

       
        if(label == "end"):
            with open('spots.txt', 'w') as file:

                for key, value in self.spot_dict.items():
                    file.write(str(key) + ":\n\t" + str(value) + "\n\n")

                response.message = "All Poses written to spots.txt file"

        else:
            self.spot_dict[label] = self.pose
            response.message = "Saved Pose for " + label + " spot"



        response.navigation_successfull = True

        return response

if __name__ == "__main__":
    rospy.init_node('spot_recorder')
    save_spots = SaveSpots()
    print("\nService Started\n")
    rospy.spin() 