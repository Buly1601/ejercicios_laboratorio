#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
import math
from turtlesim.srv import Kill



class GeometricTurleSim:

    def __init__(self):
        # x1 & y1 come from pose
        self.x1 = 0
        self.y1 = 0
        self.z1 = 0
        # x2 & y2 come from user
        self.x2 = 0
        self.y2 = 0
        self.get_from_user()
        # subscribers
        self.pose= rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        # node 
        rospy.init_node('control_turtle', anonymous=False)
        # velocity message
        self.vel_msg = Twist()
        # velocity publisher
        self.vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)



    def pose_callback(self, pose):
        # Función que se ejecuta cada vez que llega una actualización de la posición de la tortuga
        self.x1 = pose.x
        self.y1 = pose.y
        self.z1 = pose.theta

    
    def get_from_user(self):
        # get from user
        self.x2 = int(input("insert x target value: \n"))
        self.y2 = int(input("insert y target value: \n"))
    

    def geometric_calculation(self):
        # get distance to goal
        self.dtg = round(math.sqrt(((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2)), 2)
        # get angle to goal
        self.atg = math.degrees(math.atan2((self.y2-self.y1),(self.x2-self.x1)))
        # print results
        print(f"""
            DTG's value is: {self.dtg} \n
            ATG's value is: {self.atg} \n
            """)
        
    
    def spawn_in_place(self):
        kill_turtle = rospy.ServiceProxy('/kill', Kill)
        kill_turtle('turtle1') 
        spawn_turtle = rospy.ServiceProxy('spawn', Spawn)
        spawn_turtle(self.x2, self.y2, 0, "turtle1")  #x,y,theta

    
    def move_to_point(self, Kp=1.0, tolerance=0.1):

        """Moves the turtle to the specified goal position (x, y)."""
        tolerance = 0.1  # Adjust the tolerance as needed

        while True:
            distance_error = math.sqrt(pow(self.x2 - self.x1, 2) + pow(self.y2 - self.y1, 2))

            # Angular control
            angle_to_goal = math.atan2(self.y2 - self.y1, self.x2 - self.x1)
            angular_error = angle_to_goal - self.z1

            # PID control
            linear_vel = Kp * distance_error
            angular_vel = Kp * angular_error  # Simple proportional for now

            # Limit velocities for smoother movement
            linear_vel = max(min(linear_vel, 1.0), -1.0) 
            angular_vel = max(min(angular_vel, 1.5), -1.5) 

            self.vel_msg.linear.x = linear_vel
            self.vel_msg.angular.z = angular_vel
            self.vel_pub.publish(self.vel_msg)

            rospy.sleep(0.1)  # Adjust sleep time for control loop frequency

            if distance_error <= tolerance:
                break


        
if __name__ == "__main__":
    geo = GeometricTurleSim()
    
    ans = input("""insert the following:
                1. Spawn in location (a)
                2. Geometric calculation (b)
                3. Control movement (c)
                """)
    
    if ans == "a":
        geo.spawn_in_place()
    elif ans == "b":
        geo.geometric_calculation()
    elif ans == "c":
        geo.move_to_point()
    else:
        print("Unrecognized option.")