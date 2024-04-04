#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys
import select
import termios
import tty

KEYS = ["w", "a", "s", "d", "k", "l", "q"]

class TeleopTurtle:

    def __init__(self):
        self.node = rospy.init_node("control_node", anonymous=False)
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.msg = Twist()
        self.settings = termios.tcgetattr(sys.stdin)


    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key


    def teleop(self):
        while not rospy.is_shutdown():
            key = self.getKey()

            # default values
            self.msg.linear.x = 0
            self.msg.linear.y = 0
            self.msg.angular.z = 0

            # check if valid key
            if key in KEYS:
                if key == "w":
                    self.msg.linear.x = 1
                if key == "s":
                    self.msg.linear.x = -1
                if key == "a":
                    self.msg.linear.y = 1
                if key == "d":
                    self.msg.linear.y = -1
                if key == "k":
                    self.msg.angular.z = 1
                if key == "l":
                    self.msg.angular.z = -1
                if key == "q":
                    break
            
            # publish to turtle
            self.pub.publish(self.msg)
        
        
    def triangle(self, line=3, speed=1):
        # do it three times since its a triangle
        for _ in range(3):
            # setting timer now
            t_0 = rospy.Time.now().to_sec()

            # distance counter
            distance = 0 

            # only move straight
            self.msg.linear.x = speed
            self.msg.angular.z = 0
            
            while distance < line:
                # travel straight
                self.pub.publish(self.msg)

                # take current time
                t_1 = rospy.Time.now().to_sec()

                # calculate traveled distance
                distance = speed*(t_1-t_0)

            rospy.sleep(1)    
            # stop and turn
            self.msg.linear.x = 0
            self.msg.angular.z = 2.1
            self.pub.publish(self.msg)
            rospy.sleep(1)
    

    def square(self, line= 3, speed=1):
        # do it three times since its a triangle
        for _ in range(4):
            # setting timer now
            t_0 = rospy.Time.now().to_sec()

            # distance counter
            distance = 0 

            # only move straight
            self.msg.linear.x = speed
            self.msg.angular.z = 0
            
            while distance < line:
                # travel straight
                self.pub.publish(self.msg)

                # take current time
                t_1 = rospy.Time.now().to_sec()

                # calculate traveled distance
                distance = speed*(t_1-t_0)

            rospy.sleep(1)    
            # stop and turn
            self.msg.linear.x = 0
            self.msg.angular.z = 3.14/2
            self.pub.publish(self.msg)
            rospy.sleep(1)
 

if __name__ == "__main__":
    turtle = TeleopTurtle()
    turtle.teleop()
            