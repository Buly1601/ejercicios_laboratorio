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


