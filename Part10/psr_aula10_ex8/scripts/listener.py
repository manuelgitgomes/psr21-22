#!/usr/bin/python3

import rospy
import random
import std_msgs.msg
from sensor_msgs import point_cloud2
from geometry_msgs.msg import Point
from sensor_msgs.msg import LaserScan, PointField, PointCloud2
from visualization_msgs.msg import Marker, MarkerArray
from math import sin, cos

pub = rospy.Publisher('marker_array', MarkerArray, queue_size=1)

def createMarker(id):
    marker = Marker()
    marker.id = id
    marker.header.frame_id = "left_laser"
    marker.type = marker.CUBE_LIST
    marker.action = marker.ADD
    marker.scale.x = 0.2
    marker.scale.y = 0.2
    marker.scale.z = 0.2
    marker.color.r = random.random()
    marker.color.g = random.random()
    marker.color.b = random.random()
    marker.color.a = 1.0
    marker.pose.orientation.w = 1.0
    marker.pose.position.x = 0
    marker.pose.position.y = 0
    marker.pose.position.z = 0

    return marker

def chatCallback(msg):
    rospy.loginfo(" I heard Laser Scan data")
    thresh = 0.8
    marker_array = MarkerArray()
    marker = createMarker(0)
    marker_array.markers.append(marker)

    for idx, (range1, range2) in enumerate(zip(msg.ranges[:-1], msg.ranges[1:])):
        if range1 < 0.1 or range2 < 0.1:
            continue

        diff = abs(range2 - range1)

        if diff > thresh:
            marker = createMarker(idx + 1)
            marker_array.markers.append(marker)

        theta = msg.angle_min + idx * msg.angle_increment
        x = range1 * cos(theta)
        y = range1 * sin(theta)

        point = Point(x=x, y=y, z=0)

        last_marker = marker_array.markers[-1]
        last_marker.points.append(point)

    pub.publish(marker_array)



def main():
    rospy.init_node('Listener', anonymous=True)
    rospy.Subscriber('laser_scan', LaserScan, chatCallback)


    # Running again
    rospy.spin()



if __name__ == '__main__':
    main()