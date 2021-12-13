#!/usr/bin/python3

import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def main():

    # Capture webcam and create window
    capture = cv2.VideoCapture(0)
    window_name = 'A10-Ex5'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    # Defining ROS varibles
    rospy.init_node('Talker', anonymous=True)
    rate = rospy.Rate(30)
    pub = rospy.Publisher('camera', Image, queue_size=10)

    # Defining the bridge
    bridge = CvBridge()

    while not rospy.is_shutdown():
        # Capture an image from the webcam and show it
        _, image = capture.read()

        # Convert to msg and publish it
        message = bridge.cv2_to_imgmsg(image, encoding='bgr8')
        pub.publish(message)

        cv2.imshow(window_name, image)
        cv2.waitKey(1)
        rate.sleep()

if __name__ == '__main__':
    main()