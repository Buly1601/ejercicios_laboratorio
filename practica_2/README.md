# Introducción a ROS
ROS, o Robot Operating System (Sistema Operativo Robótico), es un entorno de software de código abierto que facilita la creación de software para robots. 
Se puede pensar en él como un sistema operativo similar a Windows o Linux, pero específicamente diseñado para las necesidades de la robótica.

## Ejercicio 1
Para este ejercicio, se escribieron dos programas: `talker.py` y `listener.py`. La idea es que mediante un tópico, se puedan comunicar entre sí, el talker mandará datos a listener, y listener 
imprimirá lo que recibió, si es que los datos llegaron sin problema.

### Talker
`talker.py` es el programa encargado de mandar datos para que sean recibidos e impresos en consola. Para ello, lo que se necesita hacer es usar el tópico `std_msgs.String` para mandar datos
de tipo cadena. Se crea una función que se encargará de crear el nodo, crear el publicador y mandar los datos mediante ese publicador:

```python
# crear el nodo hablador 
node = rospy.init_node("talker", anonymous=False)
# crear el publicador
pub = rospy.Publisher("chat", String, queue_size=10)
# asignar la frecuencia de datos
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    # publicar hasta que se rompa el programa
    pub.publish("hola Rocha")
    rate.sleep()
```

### Listener
`listener.py` es el programa encargado de recibir los datos de `talker.py` e imprimirlos en la consola. Para ello, éste igual se conecta al tópico `std_msgs.String`. Para que éste reciba los datos, primero se tiene que crear una función de llamado constante que se declara de la siguiente forma:

```python
def callback(msg):
    rospy.loginfo(f"escuche : {msg}")
```

Ésta función se conecta al subscriptor, después de la creación del nodo de escucha.




## Ejercicio 2
Para esta parte se creó un control por teclado para Turtlesim para que de esta forma podamos comandarlo en la cuadrícula. De igual manera, se realizó un código para que Turtlesim dibujara un cuadrado y un triángulo equilátero, todo esto sin controlador.

Como primer paso se define la clase TeleopTurtle, que inicializa el nodo de ROS, el publicador de mensajes de velocidad, la tasa de actualización y captura la configuración actual del terminal para la entrada del teclado.

```python
class TeleopTurtle:
    def __init__(self):
        self.node = rospy.init_node("control_node", anonymous=False)
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.msg = Twist()
        self.settings = termios.tcgetattr(sys.stdin)
```

Esta es una lista de teclas que el programa reconoce para controlar el movimiento del robot.

```python

KEYS = ["w", "a", "s", "d", "k", "l", "q"]
```
El método __init__ inicializa el nodo ROS, crea un publicador para enviar comandos de velocidad al robot, establece la frecuencia de publicación y prepara la estructura del mensaje Twist. También guarda la configuración actual del terminal para poder modificarla más adelante.
```python

def __init__(self):
        self.node = rospy.init_node("control_node", anonymous=False)
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.msg = Twist()
        self.settings = termios.tcgetattr(sys.stdin)
```
El método getKey se utiliza para leer una tecla presionada sin necesidad de presionar Enter. Configura el terminal en modo "raw" para capturar la entrada de teclado en tiempo real y luego lo restaura a su configuración original.
```python

def getKey(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key
```
El método teleop es el bucle principal del programa. Espera la entrada del teclado y asigna los movimientos correspondientes al robot en función de la tecla presionada. Luego publica el mensaje Twist para mover el robot.
```python

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

```

El método `triangle` permite al robot moverse formando un triángulo equilátero. Al igual que en el método `square`, este método recibe dos parámetros: `line`, que indica la longitud de cada lado del triángulo, y `speed`, que define la velocidad a la que se moverá el robot. La función realiza un bucle que se repite tres veces, correspondiente a los tres lados de un triángulo equilátero. En cada iteración del bucle, se inicia un temporizador (`t_0`) para controlar el movimiento en línea recta del robot. El robot avanza con la velocidad especificada en `speed`, manteniendo su velocidad angular en cero para asegurar un movimiento rectilíneo. La distancia recorrida se calcula continuamente usando la fórmula `distance = speed * (t_1 - t_0)`, donde `t_1` es el tiempo actual. Una vez que el robot ha completado un lado del triángulo, se detiene durante un segundo (`rospy.sleep(1)`) y luego realiza un giro para alinearse con el siguiente lado del triángulo. Este giro se logra ajustando la velocidad lineal a cero y la velocidad angular a un valor que produce un giro de 120 grados (`2.1` radianes), que es el ángulo interno de un triángulo equilátero. Tras el giro, el robot se detiene nuevamente durante un segundo antes de continuar con el siguiente lado del triángulo. Este proceso se repite hasta que el robot ha completado los tres lados, formando así un triángulo equilátero en su trayectoria.

```python

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

```
El método `square` es una función que permite al robot moverse en forma de cuadrado. Este método recibe dos parámetros: `line`, que indica la longitud de cada lado del cuadrado, y `speed`, que define la velocidad a la que se moverá el robot. La función ejecuta un bucle que se repite cuatro veces, ya que un cuadrado tiene cuatro lados. Dentro de este bucle, se utiliza un temporizador (`t_0`) para marcar el inicio del movimiento en línea recta. El robot comienza a moverse hacia adelante con la velocidad especificada en el parámetro `speed`, mientras que la velocidad angular se establece en cero para asegurar que se mueva en línea recta.

A medida que el robot avanza, el código calcula la distancia recorrida utilizando la fórmula `distance = speed * (t_1 - t_0)`, donde `t_1` es el tiempo actual. Este cálculo se realiza en un bucle interno que continúa hasta que la distancia recorrida es igual o mayor que la longitud del lado del cuadrado. Una vez que el robot ha completado un lado del cuadrado, se detiene durante un segundo (`rospy.sleep(1)`) y luego gira 90 grados para comenzar el siguiente lado. Esto se logra estableciendo la velocidad lineal a cero y la velocidad angular a un valor que corresponde a un giro de 90 grados (`3.14/2` radianes). Después de girar, el robot se detiene nuevamente durante un segundo antes de comenzar a moverse en línea recta para el siguiente lado del cuadrado. Este proceso se repite hasta que el robot ha completado los cuatro lados del cuadrado, resultando en un movimiento que traza un cuadrado en el espacio.


```python

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

```


## Ejercicio 3
Implemente un controlador PID para gestionar la posición de turtlesim.

El código implementa un controlador PID para la gestión de la posición de un robot turtle en el entorno de simulación turtlesim de ROS (Robot Operating System). La clase `MoveTurtleProportionalControl` contiene toda la lógica necesaria para controlar el movimiento del robot hacia una posición deseada.

El método `__init__` inicializa el nodo ROS, suscribe al topic de la posición actual de la tortuga, crea un publicador para enviar comandos de velocidad y establece la tasa de publicación de mensajes.
```python
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
```

El método `pose_callback` se ejecuta cada vez que se recibe una actualización de la posición de la tortuga y actualiza las variables de posición y orientación actuales.
```python
    def pose_callback(self, pose):
        # Función que se ejecuta cada vez que llega una actualización de la posición de la tortuga
        self.current_x = pose.x
        self.current_y = pose.y
        self.current_theta = pose.theta

```

El método `move_turtle_to_desired_x` recibe la posición deseada como parámetros y utiliza un bucle de control para mover el robot hacia esa posición. Dentro del bucle, se calcula el error de posición y se utiliza un controlador proporcional (con la constante Kp) para determinar la velocidad lineal y angular necesarias para corregir el error. El robot se detiene una vez que se alcanza la posición deseada dentro de un umbral definido.

```python
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

```
El método `get_desired_x_from_user`, `get_desired_y_from_user` y `get_desired_theta_from_user` se utilizan para obtener la posición deseada del usuario a través de la entrada estándar.
```python
    def get_desired_x_from_user(self):
        print("Ingrese la posición deseada en el eje x:")
        return float(input("Coordenada x: "))
    
    def get_desired_y_from_user(self):
        print("Ingrese la posición deseada en el eje y:")
        return float(input("Coordenada y: "))
    
    def get_desired_theta_from_user(self):
        print("Ingrese la posición deseada en el eje z:")
        return float(input("Coordenada z: "))

```
El método `move_turtle_to_point_sequential` utiliza un controlador PID (Proporcional-Integral-Derivativo) para mover el robot tortuga hacia una posición y orientación específicas en el plano XY. El controlador PID se utiliza para minimizar el error entre la posición y orientación deseadas y la posición y orientación actuales del robot. Este método permite un control más preciso del movimiento del robot en comparación con un simple control proporcional.

La función recibe tres parámetros: `x`, `y`, `z`, que representan las coordenadas deseadas en el plano XY y la orientación deseada en el eje Z, respectivamente.

Dentro del método, se definen las constantes de proporcionalidad (`Kp`), integral (`Ki`) y derivativa (`Kd`) del controlador PID. Estas constantes pueden ser ajustadas para obtener una respuesta de control óptima.

El método utiliza un bucle que se ejecuta hasta que el robot alcanza la posición y orientación deseadas dentro de un umbral definido. Dentro del bucle, se calculan los errores en las coordenadas X, Y y la orientación Z:

- `error_x`: la diferencia entre la posición deseada en X y la posición actual en X.
- `error_y`: la diferencia entre la posición deseada en Y y la posición actual en Y.
- `error_z`: la diferencia entre la orientación deseada en Z y la orientación actual en Z.

Para cada coordenada, se calcula la velocidad necesaria para corregir el error utilizando la fórmula del controlador PID:

- `vel_x`: la velocidad lineal en X, calculada como `Kp * error_x + Ki * error_accumulation_x + Kd * (error_x - last_error_x)`.
- `vel_y`: la velocidad lineal en Y, calculada de manera similar a `vel_x`.
- `vel_z`: la velocidad angular en Z, calculada utilizando la misma fórmula que para las velocidades lineales.

Después de calcular las velocidades, se crea un mensaje de tipo `Twist` que contiene las velocidades calculadas y se publica en el topic `/turtle1/cmd_vel` para mover el robot.

El método también registra en el terminal la posición actual, el error y la velocidad lineal para fines de depuración.

El bucle continúa hasta que los errores en X, Y y Z son menores que un umbral definido, lo que indica que el robot ha alcanzado la posición y orientación deseadas. En ese punto, el método termina y el robot se detiene.

```python
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

```
El método `move_turtle_interactively` permite al usuario introducir repetidamente posiciones deseadas y mueve el robot a esas posiciones utilizando el método `move_turtle_to_point_sequential`.
```python
    def move_turtle_interactively(self):
        while not rospy.is_shutdown():
            # Obtener la posición deseada del usuario
            desired_x = self.get_desired_x_from_user()
            desired_y = self.get_desired_y_from_user()
            desired_theta = self.get_desired_theta_from_user()

            # Mover la tortuga a la posición deseada
            self.move_turtle_to_point_sequential(desired_x, desired_y, desired_theta)

```
Finalmente, en el bloque `if __name__ == '__main__':`, se crea una instancia de `MoveTurtleProportionalControl` y se llama al método `move_turtle_interactively` para iniciar el control interactivo del robot.
```python
if __name__ == '__main__':
    try:
        move_turtle_proportional = MoveTurtleProportionalControl()
        move_turtle_proportional.move_turtle_interactively()
    except rospy.ROSInterruptException:
        pass

```


