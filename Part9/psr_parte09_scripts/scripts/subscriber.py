#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String
from psr_parte09_scripts.msg import Dog


def callbackMsgReceived(msg):
    print("Received a dog named " + msg.name + ' which is ' + str(msg.age) +
                  ' years old')
    rospy.loginfo("Received a dog named " + msg.name + ' which is ' + str(msg.age) +
                  ' years old')


def main():
    # ---------------------------------------------------
    # Initialization
    # ---------------------------------------------------
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('chatter', Dog, callbackMsgReceived) # configure the subscriber

    # create a dog message to send
    dog = Dog()
    dog.name = 'dog3'
    dog.age = 1
    dog.color = 'black'

    rospy.spin()

if __name__ == '__main__':
    main()
