#!/usr/bin/env python


import sys
import rospy
import tf
import moveit_commander 
import random
from geometry_msgs.msg import Pose, Point, Quaternion
from math import pi

pose_goal = Pose()
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('ur3_move',anonymous=True)
group = [moveit_commander.MoveGroupCommander("manipulator")]  # ur3 moveit group name: manipulator

while not rospy.is_shutdown():
	x_pos = input("Insert X value:")
	y_pos = input("Insert Y value:")
	z_pos = input("Insert Z value:")
	print(x_pos,y_pos,z_pos)
	pose_goal.orientation.w = 1.0
	pose_goal.position.x = x_pos  
	pose_goal.position.y = y_pos  
	pose_goal.position.z = z_pos 
	group[0].set_pose_target(pose_goal)
	group[0].go(True)
	rospy.sleep(2)
 

moveit_commander.roscpp_shutdown()
