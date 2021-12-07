#!/usr/bin/python3

import rospy
import argparse
from std_msgs.msg import String
from psr_aula8_ex5.msg import Dog
from psr_aula8_ex5.srv import SetDogName, SetDogNameRequest, SetDogNameResponse


def main():
    # Create argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('-n', '--name', required=True, help="Name of the dog")
    args = vars(ap.parse_args())

    rospy.wait_for_service('set_dog_name')

    try:
        set_dog_name = rospy.ServiceProxy('set_dog_name', SetDogName)
        resp1 = set_dog_name(args['name'])
        print(resp1)
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)



if __name__ == '__main__':
    main()