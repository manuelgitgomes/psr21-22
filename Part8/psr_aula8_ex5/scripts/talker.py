#!/usr/bin/python3

import rospy
import argparse
from std_msgs.msg import String
from psr_aula8_ex5.msg import Dog
from psr_aula8_ex5.srv import SetDogName, SetDogNameRequest, SetDogNameResponse

def handle_set_dog_name(req):
    global new_name
    new_name = req.new_name
    rospy.loginfo("The dog's new name will be: " + new_name)
    return True

def main():
    global new_name
    new_name = None

    # Create argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--publisher', required=True, help="Name of the topic to publish to")
    args = vars(ap.parse_args())

    # Initiating ros node, rate and publisher
    publisher = args['publisher']
    rospy.init_node('Talker', anonymous=True)
    rate = rospy.Rate(10)
    pub = rospy.Publisher(publisher, Dog, queue_size=10)
    s = rospy.Service('set_dog_name', SetDogName, handle_set_dog_name)


    # Defining the message
    message = Dog()
    message.name = 'Stoutland'
    message.age = 12
    message.color = 'Brown'
    message.brothers = ['Herdier', 'Lillipup']

    while not rospy.is_shutdown():
        if new_name is not None:
            print('test')
            message.name = new_name
        rospy.loginfo(message)
        pub.publish(message)
        new_name = None
        rate.sleep()


if __name__ == '__main__':
    main()