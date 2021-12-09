#!/usr/bin/python3

import rospy
import argparse
import std_msgs.msg
from sensor_msgs import point_cloud2
from sensor_msgs.msg import LaserScan, PointField, PointCloud2
from math import sin, cos

pub = rospy.Publisher('pointcloud', PointCloud2)

def chatCallback(msg):
    rospy.loginfo(" I heard Laser Scan data")
    header = std_msgs.msg.Header(seq=msg.header.seq, stamp=msg.header.stamp, frame_id=msg.header.frame_id)
    fields = [PointField('x', 0, PointField.FLOAT32, 1),
              PointField('y', 4, PointField.FLOAT32, 1),
              PointField('z', 8, PointField.FLOAT32, 1)]

    points = []
    z = 0
    for idx, range in enumerate(msg.ranges):
        theta = msg.angle_min + idx * msg.angle_increment
        x = range * cos(theta)
        y = range * sin(theta)
        points.append((x, y, z))

    # pcloud = PointCloud2()
    pcloud = point_cloud2.create_cloud(header, fields, points)
    # pcloud.header = header
    # pcloud.fields = fields
    # pcloud.data = points
    pub.publish(pcloud)
        

def main():
    rospy.init_node('Listener', anonymous=True)
    rospy.Subscriber("laser_scan_topic", LaserScan, chatCallback)


    # Running again
    rospy.spin()



if __name__ == '__main__':
    main()