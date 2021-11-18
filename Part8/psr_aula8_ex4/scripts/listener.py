#!/usr/bin/python3

import rospy
import argparse
from psr_aula8_ex4.msg import Dog


def chatCallback(data):
    rospy.loginfo("Name of the dog: %s", data.name)
    rospy.loginfo("Age of the dog: %s", data.age)
    rospy.loginfo("Colour of the dog: %s", data.color)
    rospy.loginfo("Brothers of the dog: %s", data.brothers)


def main():
    # Create argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('-s', '--subscriber', required=True, help="Name of the topic to subscribe to")
    args = vars(ap.parse_args())

    # Initiating ros node and subscriber
    subscriber = args['subscriber']
    rospy.init_node('Listener', anonymous=True)
    rospy.Subscriber(subscriber, Dog, chatCallback)

    # Running again
    rospy.spin()



if __name__ == '__main__':
    main()