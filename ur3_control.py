#!/usr/bin/env python

# Author : Maroine Trabelsi
# trabelsi.maroine@gmail.com
# init : 03 May 2020

import sys
import rospy
import tf
import moveit_commander
import random
from geometry_msgs.msg import Pose, Point, Quaternion
from math import pi

import moveit_msgs.msg

group_name = "manipulator"
pose_goal = Pose()
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('ur3_move',anonymous=True)
group = [moveit_commander.MoveGroupCommander(group_name)]

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory,queue_size=20)

pose_goal.orientation.w = 0.0
pose_goal.position.x = 0.2
pose_goal.position.y = 0.0
pose_goal.position.z = 0.2

# Initial pose
group[0].set_pose_target(pose_goal)
group[0].go(True)

rospy.sleep(1)

print("UR3 Control Robot commander")
print("Available commands : ")
print(" W - move X forward")
print(" S - move X backward")
print(" A - move Y left")
print(" D - move Y right")
print(" R - move Z left")
print(" F - move Z right")



while not rospy.is_shutdown():
	command = raw_input("Control : ")
	if command == 'w':		
		pose_goal.orientation.w = 0.0
		pose_goal.position.x = pose_goal.position.x + 0.05
		pose_goal.position.y = pose_goal.position.y
		pose_goal.position.z = pose_goal.position.z
		group[0].set_pose_target(pose_goal)
		group[0].go(True)
	elif command == 's':
		pose_goal.orientation.w = 0.0
		pose_goal.position.x = pose_goal.position.x - 0.05
		pose_goal.position.y = pose_goal.position.y
		pose_goal.position.z = pose_goal.position.z
		group[0].set_pose_target(pose_goal)
		group[0].go(True)
	elif command == 'a':
		pose_goal.orientation.w = 0.0
		pose_goal.position.x = pose_goal.position.x
		pose_goal.position.y = pose_goal.position.y - 0.05
		pose_goal.position.z = pose_goal.position.z
		group[0].set_pose_target(pose_goal)
		group[0].go(True)
	elif command == 'd':
		pose_goal.orientation.w = 0.0
		pose_goal.position.x = pose_goal.position.x
		pose_goal.position.y = pose_goal.position.y + 0.05
		pose_goal.position.z = pose_goal.position.z
		group[0].set_pose_target(pose_goal)
		group[0].go(True)
	elif command == 'r':
		pose_goal.orientation.w = 0.0
		pose_goal.position.x = pose_goal.position.x
		pose_goal.position.y = pose_goal.position.y
		pose_goal.position.z = pose_goal.position.z + 0.05
		group[0].set_pose_target(pose_goal)
		group[0].go(True)
	elif command == 'f':
		pose_goal.orientation.w = 0.0
		pose_goal.position.x = pose_goal.position.x
		pose_goal.position.y = pose_goal.position.y
		pose_goal.position.z = pose_goal.position.z - 0.05
		group[0].set_pose_target(pose_goal)
		group[0].go(True)

	print("Position : ",pose_goal.position.x, pose_goal.position.y , pose_goal.position.z)
	rospy.sleep(0.5)


moveit_commander.roscpp_shutdown()
