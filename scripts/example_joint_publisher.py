#!/usr/bin/python3.8
"""
    This script was design and implemented by
    github: AndresRoc (https://github.com/AndresRoc)
"""
import rospy
from std_msgs.msg import Float64, Float64MultiArray

def jointAngle(joint_position):
    pub = [rospy.Publisher('/franka/joint{}_position_controller/command'.format(i), Float64, queue_size=10) for i in range(1, 8)]
    rospy.init_node('example_joint_publisher')
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo(joint_position)
        pub.publish(joint_position)
        rate.sleep()

if __name__ == '__main__':
    try:
        joint_position = [0, 0, 0, -0.5, 0, 0.5, 0.75]
        jointAngle(joint_position)
    except rospy.ROSInterruptException:
        rospy.loginfo("failed")
        pass