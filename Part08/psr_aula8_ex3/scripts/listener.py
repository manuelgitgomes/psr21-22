#!/usr/bin/python3

import rospy
import argparse
from std_msgs.msg import String


def chatCallback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.data)


def main():
    # Create argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('-s', '--subscriber', required=True, help="Name of the topic to subscribe to")
    args = vars(ap.parse_args())

    # Initiating ros node and subscriber
    subscriber = args['subscriber']
    rospy.init_node('Listener', anonymous=True)
    rospy.Subscriber(subscriber, String, chatCallback)

    # Running again
    rospy.spin()



if __name__ == '__main__':
    main()