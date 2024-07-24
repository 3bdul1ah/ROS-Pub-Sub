#!/usr/bin/env python3

import rospy                                                                  # Importing rospy library for ROS Python                                              
from std_msgs.msg import String                                               # Importing String message type from std_msgs
                            
def my_callback(my_string):                                                   # Callback function to handle incoming messages

    rospy.loginfo(rospy.get_caller_id() + " I heard %s", my_string.data)

def listener():                                                               # Function to initialize the node and set up a subscriber

    rospy.init_node('listener', anonymous=True)                               # Initializing a ROS node named 'listener' with anonymous=True to ensure unique node names               
    rospy.Subscriber('Chat', String, my_callback)                             # Creating a Subscriber to listen for String messages on 'Chat' topic with the my_callback function as the callback
  
    rospy.spin()                                                              # Keep listening (like while true)
if __name__ == "__main__":
    listener()


"""

ROS Command for Subscriber:
--------------------------------------------------------------------------------------------------------------
def callback_function(message):
    # Log information about the received message
    rospy.loginfo(rospy.get_caller_id() + " ...")

    # Access fields of the message (replace 'X' with actual fields from 'message')
    # Use 'rosmsg show <MessageType>' to inspect message structure
    # Example: If the message has fields 'x', 'y', 'theta', access them as message.x, message.y, message.theta
    # Example usage: rospy.loginfo("Received x: %s, y: %s", message.x, message.y)
    
rospy.init_node('node_name', anonymous=True)
rospy.Subscriber('topic_name', MessageType, callback_function)
rospy.spin() 
--------------------------------------------------------------------------------------------------------------

"""
