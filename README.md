# Ejercicios del laboratorio del curso LRT4102
En este repositorio se encuentran las diferentes prácticas desarrolladas en el laboratorio de la clase de Diseño de sistemas robóticos con la clave LRT4102 en la Universidad de las Américas Puebla.

## Práctica 1
En esta práctica, se introdujo Python y se resolvieron diferentes ejercicios relacionados a lo básico de Python.
Los problemas se encuentran en este [documento](https://winliveudlap-my.sharepoint.com/:b:/r/personal/charbel_breydyts_udlap_mx/Documents/Rob%C3%B3tica%20y%20Telecomunicaciones/Octavo%20Semestre/Robotica%20Aplicada/lab/Intro%20Python.pdf?csf=1&web=1&e=73IES7).

## Práctica 2
En esta práctica, se introdujo ROS, así como la introducción al turtlesim para llegar de un punto `A` un punto `B`, usando controladores PID. Los problemas se encuentran en este [documento]()

### Uso y descarga de la práctica 2
Ya que lo que se encuentra en la carpeta `practica_2` son solo programas en Python, no se podrán usar de forma normal ya que están directamente conectados a ROS, para hacer uso de ellos, se necesita seguir los siguientes pasos:
- Ir a la carpeta llamada `catkin_ws`: `cd ~/catkin_ws/`
- Ir a la carpeta llamada `/src`: `cd src/`
- Crear un nuevo paquete dentro de catkin: `catkin_create_pkg nombre_de_carpeta rospy std_msgs`
- Clonar los códigos dentro de la carpeta creada.
