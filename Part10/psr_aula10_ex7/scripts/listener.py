#!/usr/bin/python3

import rospy
from visualization_msgs.msg import Marker


def main():
    rospy.init_node('Listener', anonymous=True)
    pub = rospy.Publisher('marker', Marker, queue_size=10)
    rate = rospy.Rate(10)

    # Defining markers
    marker1 = Marker()
    marker1.id = 1
    marker1.header.frame_id = "map"
    marker1.type = marker1.CUBE
    marker1.action = marker1.ADD
    marker1.scale.x = 0.2
    marker1.scale.y = 0.2
    marker1.scale.z = 0.2
    marker1.color.r = 1.0
    marker1.color.g = 0.0
    marker1.color.b = 0.0
    marker1.color.a = 1.0
    marker1.pose.orientation.w = 1.0
    marker1.pose.position.x = 0
    marker1.pose.position.y = 0

    rospy.loginfo('Marker1 defined')

    marker2 = Marker()
    marker2.id = 2
    marker2.header.frame_id = "map"
    marker2.type = marker2.SPHERE
    marker2.action = marker2.ADD
    marker2.scale.x = 1
    marker2.scale.y = 1
    marker2.scale.z = 1
    marker2.color.r = 0.0
    marker2.color.g = 1.0
    marker2.color.b = 0.0
    marker2.color.a = 0.5
    marker2.pose.orientation.w = 1.0
    marker2.pose.position.x = 0
    marker2.pose.position.y = 0

    rospy.loginfo('Marker2 defined')

    marker3 = Marker()
    marker3.id = 3
    marker3.header.frame_id = "map"
    marker3.type = marker3.TEXT_VIEW_FACING
    marker3.action = marker3.ADD
    marker3.scale.x = 0.4
    marker3.scale.y = 0.4
    marker3.scale.z = 0.4
    marker3.color.r = 0.0
    marker3.color.g = 1.0
    marker3.color.b = 0.0
    marker3.color.a = 0.5
    marker3.pose.orientation.w = 1.0
    marker3.pose.position.x = 3
    marker3.pose.position.y = 3
    marker3.text = 'Radius: 0.4'

    rospy.loginfo('Marker3 defined')

    while not rospy.is_shutdown():
        pub.publish(marker1)
        pub.publish(marker2)
        pub.publish(marker3)
        rospy.loginfo('All published')
        rate.sleep()



if __name__ == '__main__':
    main()