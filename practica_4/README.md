# URDF y PlotJuggler
## URDF
El URDF (Unified Robot Description Format) es un formato de archivo utilizado en ROS (Robot Operating System) para describir la estructura cinemática y visual de robots.

En esencia, el URDF proporciona una forma estándar de representar la geometría del robot, así como su cinemática, es decir, la forma en que sus partes móviles están conectadas y pueden moverse en relación con otras partes. Esto incluye información sobre enlaces (links), articulaciones (joints), sensores y visualización.

El URDF se utiliza para modelar robots tanto en simulaciones como en el mundo real. Es especialmente útil en el desarrollo y la simulación de aplicaciones robóticas, ya que permite a los desarrolladores visualizar y simular el comportamiento de los robots antes de implementarlos físicamente. Además, el URDF es compatible con herramientas de visualización como RViz, que permite a los usuarios visualizar el modelo del robot y realizar análisis cinemáticos.





## PlotJuggler
Para este ejercicio se pidió graficar el movimiento, error y ATG y DGT usando la herramienta de [PlotJuggler](https://plotjuggler.io/).
Para ello, se tiene que inicializar PlotJuggler siguiendo los siguientes pasos:
- Descargar PlotJuggler si es necesario, usando el link anterior.
- Correr el comando `rosrun plotjuggler plotjuggler -t`.
- Seguir los pasos de la `practica_3`.
- En la ventana izquierda de PlotJuggler, dar click en `ROS topic subscriber` y seleccionar `/turtle1/ṕose`.
- Seleccionar del árbol `x` y `y`. 

### Ploteo de la posición y error del turtlesim
Al correr el programa de la `practica_3`, se plotearon las siguientes gráficas:

![X y Y del turtlesim hacia (0,0)](https://github.com/Buly1601/ejercicios_laboratorio/blob/main/practica_4/x%26y.png)
Se puede observar en ella que los dos la velocidad de `X` y `Y` sube y baja de forma curva, y llega a 0, por lo tanto se puede apreciar que el error es 0 ya que las velocidades decrecen al llegar al punto deseado (0,0).

![Posición del turtlesim](https://github.com/Buly1601/ejercicios_laboratorio/blob/main/practica_4/xysim.png)
Se puede observar que el comportamiento de la gráfica es igual al del turtlesim, se llega al punto deseado.

### Plotear ATG y DTG
Para este ejercicio, se 
