#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('test_sub_node')

def sometopic_callback(msg):
    rospy.loginfo('got msg: %s' % msg)

sub = rospy.Subscriber('atopic', String, sometopic_callback)

rospy.spin()
