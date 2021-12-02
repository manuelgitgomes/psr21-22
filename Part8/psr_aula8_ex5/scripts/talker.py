#!/usr/bin/python3

import rospy
import argparse
from std_msgs.msg import String
from psr_aula8_ex5.msg import Dog
from psr_aula8_ex5.srv import SetDogName, SetDogNameRequest, SetDogNameResponse

def main():
    # Create argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--publisher', required=True, help="Name of the topic to publish to")
    args = vars(ap.parse_args())

    # Initiating ros node, rate and publisher
    publisher = args['publisher']
    rospy.init_node('Talker', anonymous=True)
    rate = rospy.Rate(10)
    pub = rospy.Publisher(publisher, Dog, queue_size=10)
    s = rospy.Service('add_two_ints', SetDogName, handle_set_dog_name)

    # Defining the message
    message = Dog()
    message.name = 'Stoutland'
    message.age = 12
    message.color = 'Brown'
    message.brothers = ['Herdier', 'Lillipup']

    while not rospy.is_shutdown():
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()


if __name__ == '__main__':
    main()