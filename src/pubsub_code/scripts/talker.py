#!/usr/bin/env python3

import rospy                                                   # Importing rospy library for ROS Python                                 
from std_msgs.msg import String                                # Importing String message type from std_msgs
              
def talker():
    rospy.init_node('talker', anonymous=True)                  # Initializing a ROS node named 'talker' with anonymous=True to ensure unique node names
    pub = rospy.Publisher('Chat', String, queue_size=10)       # Creating a publisher to publish String messages on 'Chat' topic with a queue size of 10
    rate = rospy.Rate(10)                                      # Setting the publish rate to 10Hz
                              
    while not rospy.is_shutdown():                             # Loop until shutdown (Ctrl+C is pressed)
                         
        test_str = "Test ROS %s" % rospy.get_time()            # Generating a test message with current time
        rospy.loginfo(test_str)                                # Logging the message to rospy (similar to print but for ROS)   
        pub.publish(test_str)                                  # Publishing the message on the 'Chat' topic        
        rate.sleep()                                           # Sleeping according to the rate to maintain the specified frequency
   
if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


"""

ROS Syntax for Publisher:
----------------------------------------------------------------
rospy.init_node('node_name', anonymous=True)
rospy.Publisher('topic_name', MessageType, queue_size=queue_size)
rate = rospy.Rate(rate_hz)
rospy.loginfo(message)
pub.publish(message)
rate.sleep()
----------------------------------------------------------------

""" 

