import rospy
from std_msgs.msg import String

def talker():
    # create conncections
    node = rospy.init_node("talker", anonymous=False)
    pub = rospy.Publisher("chat", String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pub.publish("hola Rocha")
        rate.sleep()


if __name__ == "__main__":
    try:
        talker()
    except:
        pass
