#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math


class MoveTurtleProportionalControl:
    def __init__(self):
        rospy.init_node('control_tortuga_x')
        
        # Suscribirse al topic de la posición de la tortuga
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        
        # Publicar en el topic de comandos de movimiento de la tortuga
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        
        # Tasa de publicación de mensajes (10 Hz)
        self.rate = rospy.Rate(10)
        
        self.current_x = 0
        self.current_y = 0
        self.current_theta = 0

        # twist obj
        self.twist_msg = Twist()


    def pose_callback(self, pose):
        # Función que se ejecuta cada vez que llega una actualización de la posición de la tortuga
        self.current_x = pose.x
        self.current_y = pose.y
        self.current_theta = pose.theta


    def move_turtle_to_desired_x(self, desired_x, desired_y, desired_theta):
        # Constante de proporcionalidad del controlador (ajustable)
        Kp = 1

        while not rospy.is_shutdown():
            #distance = abs(math.sqrt(((desired_x - self.current.x) ** 2) + (desired_y - self.current.y) ** 2))
            des_angle_goal = math.atan2(desired_y - self.current_y, desired_x - self.current_x)
            

            # Calcular el error de posición
            error_x = desired_x - self.current_x
            error_y = desired_y - self.current_y
            error_theta = desired_theta - self.current_theta
            
            # Calcular la velocidad lineal del movimiento
            vel_x = Kp * error_x
            vel_y = Kp * error_y
            #vel_theta = (des_angle_goal - self.current_theta) * Kp
            vel_theta = des_angle_goal * error_theta
            
            # mensaje
            twist_msg = Twist()

            # Crear un mensaje de Twist para enviar el comando de movimiento
            twist_msg.linear.x = vel_x
            twist_msg.linear.y = vel_y
            twist_msg.angular.z = vel_theta
            self.velocity_publisher.publish(twist_msg)
            
            # Publicar el mensaje
            self.velocity_publisher.publish(twist_msg)
            
            # Imprimir la posición actual, el error y la variable vel_x en la terminal
            rospy.loginfo("Posición actual: %f, Error: %f, Velocidad lineal: %f", self.current_x, error_theta, vel_theta)
            
            # Verificar si se alcanza la posición deseada
            if abs(error_x) < 0.1 and abs(error_y) < 0.1 and abs(error_theta) < 0.1:
                rospy.loginfo("Posición deseada alcanzada")
                break
            
            # Esperar hasta la siguiente iteración
            self.rate.sleep()

    def get_desired_x_from_user(self):
        print("Ingrese la posición deseada en el eje x:")
        return float(input("Coordenada x: "))
    
    def get_desired_y_from_user(self):
        print("Ingrese la posición deseada en el eje y:")
        return float(input("Coordenada y: "))
    
    def get_desired_theta_from_user(self):
        print("Ingrese la posición deseada en el eje z:")
        return float(input("Coordenada z: "))
    

    def move_turtle_to_point_sequential(self, x, y, z):
        # Constantes de proporcionalidad, integral y derivativa del controlador (ajustables)
        Kp = 1
        Ki = 0.01
        Kd = 0.1

        error_accumulation_x = 0
        error_accumulation_y = 0
        error_accumulation_z = 0
        last_error_x = 0
        last_error_y = 0
        last_error_z = 0
        error_x = 1
        error_y = 1
        error_z = 1
        past_z = 0

        while not rospy.is_shutdown():
            # move first in x-y directions
            # get error
            # correct to 0 always
            while abs(error_z) > 0.01:
                error_z = -past_z - self.current_theta
                # Calcular la velocidad lineal del movimiento
                vel_z = Kp * error_z + Ki * error_accumulation_z + Kd * (error_z - last_error_z)
                # Guardar el error actual para usarlo en la próxima iteración
                last_error_z = error_z
                # send to turtle
                self.twist_msg.angular.z = vel_z
                self.velocity_publisher.publish(self.twist_msg)

                
            while abs(error_x) > 0.01:
                error_x = x - self.current_x
                # Calcular la velocidad lineal del movimiento
                vel_x = Kp * error_x + Ki * error_accumulation_x + Kd * (error_x - last_error_x)
                # Guardar el error actual para usarlo en la próxima iteración
                last_error_x = error_x
                # send to turtle
                self.twist_msg.linear.x = vel_x
                self.velocity_publisher.publish(self.twist_msg)
            
            while abs(error_y) > 0.01:
                error_y = y - self.current_y
                # Calcular la velocidad lineal del movimiento
                vel_y = Kp * error_y + Ki * error_accumulation_y + Kd * (error_y - last_error_y)
                # Guardar el error actual para usarlo en la próxima iteración
                last_error_y = error_y
                # send to turtle
                self.twist_msg.linear.y = vel_y
                self.velocity_publisher.publish(self.twist_msg)

            while abs(error_z) > 0.01:
                error_z = z - self.current_theta
                # Calcular la velocidad lineal del movimiento
                vel_z = Kp * error_z + Ki * error_accumulation_z + Kd * (error_z - last_error_z)
                # Guardar el error actual para usarlo en la próxima iteración
                last_error_z = error_z
                # send to turtle
                self.twist_msg.angular.z = vel_z
                self.velocity_publisher.publish(self.twist_msg)
            past_z = z

            
            # Imprimir la posición actual, el error y la variable vel_x en la terminal
            rospy.loginfo("Posición actual: %f, Error: %f, Velocidad lineal: %f", self.current_x, error_x, vel_x)
            
            # Verificar si se alcanza la posición deseada
            if abs(error_x) < 0.1 and abs(error_y) < 0.1 and abs(error_z) < 0.1:
                rospy.loginfo("Posición deseada alcanzada")
                break
            
            # Esperar hasta la siguiente iteración
            self.rate.sleep()
    

    def move_turtle_interactively(self):
        while not rospy.is_shutdown():
            # Obtener la posición deseada del usuario
            desired_x = self.get_desired_x_from_user()
            desired_y = self.get_desired_y_from_user()
            desired_theta = self.get_desired_theta_from_user()

            # Mover la tortuga a la posición deseada
            self.move_turtle_to_point_sequential(desired_x, desired_y, desired_theta)

        

if __name__ == '__main__':
    try:
        move_turtle_proportional = MoveTurtleProportionalControl()
        move_turtle_proportional.move_turtle_interactively()
    except rospy.ROSInterruptException:
        pass