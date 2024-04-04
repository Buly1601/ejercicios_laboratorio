import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(f"escuche : {msg}")

def listener():
    node = rospy.init_node("listener", anonymous=False)
    sub = rospy.Subscriber("chat", String, callback)
    rospy.spin()


if __name__ == "__main__":
    listener()