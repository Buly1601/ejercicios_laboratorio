# Control con ROS
El control con ROS (Robot Operating System) se refiere a la utilización de este robusto framework de software para gestionar y comandar robots de forma eficiente. ROS proporciona una arquitectura modular y flexible que permite a los desarrolladores diseñar y ejecutar controladores robóticos de manera organizada y escalable.

Los ejercicios se encuentran en el mismo archivo de Python: `geometrico.py`, en ella se encuentra la clase `GeometricTurtleSim` en la que se encuentran los ejercicios como métodos.

## Ejercicio 1
Para este ejercicio, se pidió que se calculara y mostrara en pantalla la `Distance To Goal` y el `Angle To Goal`. 
El DTG se calcula con la siguiente fórmula:
```math
DTG = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} $$
```
El ATG se calcula con la siguiente fórmula:
```math
ATG = \arctan{(y_2 - y_1), (x_2 - x_1)}
```
Esto se puede observar en el método `geometric_calculation()` dentro de la clase. Para obtener los valores que se desean obtener del usuario, `x2` y `y2` se usa el método `get_from_user()` el cual guarda en las variables `self.x2` y `self.y2` los valores del usuario.

## Ejercicio 2
Para este ejercicio, se pidió originar el turtlesim en las coordenadas que el usuario pidiera, es decir, spawnear la tortuga en donde se desee sin que haga algún tipo de movimiento. Para resolverlo, se siguieron los siguientes pasos:
- Desaparecer a la tortuga original que nace en `(5,5)` usando `rospy.ServiceProxy('/kill', Kill)`.
- Crear una tortuga nueva en las coordenadas que se desean usando `rospy.ServiceProxy('/spawn', Spawn)`.

