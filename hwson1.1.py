#!/usr/bin/env python
import rospy
from ros_tuttorials.msg import Route
from turtlesim.msg import Pose
import math
import time

class turtlesim():
	def __init__(self):
		rospy.init_node("move_turtle", anonymous = True)
		self.velocity_publisher = rospy.Publisher("/turtle1/cmd_vel", Route, queue_size = 10)
		self.pose_subscriber = rospy.Subscriber("turtle1/pose", Pose, self.poseCallback)
		self.pose = Pose()

	def poseCallback(self, data):
		self.pose.x = round(data, x, 1)
		rospy.loginfo("theta = %f \n", self.pose.x)
	
	def move(self):
		vel_msg = Route()
		vel_msg.linear.x = 1
		vel_msg.angular.z = 0
		rate = rospy.Rate(10)
		while self.pose.x < 10:
			if self.pose.x == 10:
				break
			self.velocity_publisher.publish(vel_msg)
			rate.sleep()
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		self.velocity_publisher.publish(vel_msg)
		rospy.loginfo("Done")
		rate.sleep()
	

if __name__ == "__main__" :
	try:
		x = turtlesim#!/usr/bin/env python
import rospy
from ros_tuttorials.msg import Route
from turtlesim.msg import Pose
import math
import time

class turtlesim():
	def __init__(self):
		rospy.init_node("move_turtle", anonymous = True)
		self.velocity_publisher = rospy.Publisher("/turtle1/cmd_vel", Route, queue_size = 10)
		self.pose_subscriber = rospy.Subscriber("turtle1/pose", Pose, self.poseCallback)
		self.pose = Pose()

	def poseCallback(self, data):
		self.pose.x = round(data, x, 1)
		rospy.loginfo("theta = %f \n", self.pose.x)
	
	def move(self):
		vel_msg = Route()
		vel_msg.linear.x = 1
		vel_msg.angular.z = 0
		rate = rospy.Rate(10)
		while self.pose.x < 10:
			if self.pose.x == 10:
				break
			self.velocity_publisher.publish(vel_msg)
			rate.sleep()
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		self.velocity_publisher.publish(vel_msg)()
		x.move()

		rospy.init_node("move_turtle", anonymous= True)

		route_topic = "/turtle1/cmd_vel"
		velocity_publisher = rospy.Publisher(cmd_vel_topic, Route, queue_size = 10)

		position_topic = "/turtle1/pose"
		pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
		time.sleep(2)


		move(velocity_publisher)

	except rospy.ROSInterruptException:
		rospy.loginfo("node terminated")


