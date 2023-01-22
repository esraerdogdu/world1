#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math
import time
from turtlesim.msg import Pose


def location (velocity_publisher, angular_speed_degree, relative_angle_degree, clockwise):

	velocity_message = Twist()
	
	angular_speedmath.radians(abs(angular_speed_degree))


	if (clockwise):
		velocity_message.angular.z = -abs(angular_speed)
	else:
		velocity_message.angular.z = abs(angular_speed)

	loop_rate = rospy.Rate(10)
	current_time = rospy.Time.now().to_sec()


	while True:
		rospy.loginfo("Turtlesim moves")
		velocity_publisher.publish(velocity_message)

		new_time = rospy.Time.now().to_sec()
		current_angle_degree = (new_time - current_time) * angular_speed_degree
		loop_rate.sleep()

		if (current_angle_degree > relative_angle_degree) :
			rospy.loginfo("reached")
			break


	velocity_message.angular.z = 0
	velocity_publisher.publish(velocity_message)

if __name__ == "__main__" :
	try:

		rospy.init_node("turtlesim_motion_pose", anonymous= True)

		cmd_vel_topic = "/turtle1/cmd_vel"
		velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

		position_topic = "/turtle1/pose"
		pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
		time.sleep(2)

		location(velocity_publisher, 30, 90, True)

	except rospy.ROSInterruptException:
		rospy.loginfo("node terminated")