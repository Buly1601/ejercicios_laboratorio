# URDF y PlotJuggler
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
