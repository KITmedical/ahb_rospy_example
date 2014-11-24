#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('test_pub_node')

pub = rospy.Publisher('atopic', String, queue_size = 1)

while not rospy.is_shutdown():
  stringMsg = String()
  stringMsg.data = 'foo'
  pub.publish(stringMsg)

  rospy.sleep(1.0)
