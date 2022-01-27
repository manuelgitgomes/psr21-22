#!/usr/bin/python3

import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import TransformStamped
import tf2_ros


def modelStatesMsgCallback(msg):
    player_name = 'p_mgomes'
    br = tf2_ros.TransformBroadcaster()
    t = TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "world"
    t.child_frame_id = f'{player_name}/base_footprint'
    idx = [idx for idx, i in enumerate(msg.name) if i == player_name]
    t.transform.translation = msg.pose[idx[0]].position
    t.transform.rotation = msg.pose[idx[0]].orientation
    br.sendTransform(t)


def main():

    # Initiating node
    rospy.init_node('model_states_to_tf', anonymous=False)

    # Defining buffer
    tf_buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tf_buffer)


    # Defining the subscriber
    rospy.Subscriber('/gazebo/model_states', ModelStates, modelStatesMsgCallback)

    rospy.spin()


if __name__ == '__main__':
    main()
