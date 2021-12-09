#!/usr/bin/python3

import rospy
import argparse
from std_msgs.msg import String


def main():
    # Create argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--publisher', required=True, help="Name of the topic to publish to")
    args = vars(ap.parse_args())

    # Initiating ros node, rate and publisher
    publisher = args['publisher']
    rospy.init_node('Talker', anonymous=True)
    rate = rospy.Rate(10)
    pub = rospy.Publisher(publisher, String, queue_size=10)
    while not rospy.is_shutdown():
        print('Print a message: ')
        message = input()
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()


if __name__ == '__main__':
    main()