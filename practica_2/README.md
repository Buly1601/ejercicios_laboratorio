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

```python
def listener():
    node = rospy.init_node("listener", anonymous=False)
    sub = rospy.Subscriber("chat", String, callback)
    rospy.spin()
```
