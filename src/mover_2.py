#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
#Cambio en la rama develop

def move_turtle():
    # Inicializa el nodo de ROS llamado "move_turtle"
    rospy.init_node('move_turtle', anonymous=True)

    # Crea un objeto para publicar mensajes de Twist (velocidad lineal y angular)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Crea un objeto de tipo Twist
    twist = Twist()
    
    # Configura las velocidades
    twist.linear.x = 2.0  # Velocidad lineal hacia adelante
    twist.angular.z = 0.5  # Velocidad angular (giro)

    # Establece la frecuencia de publicación en 10 Hz (cada 0.1 segundos)
    rate = rospy.Rate(10)  # 10 Hz
    # Espera un poco para que el movimiento ocurra
    rospy.sleep(2)

    # Detiene la tortuga
    twistd = Twist()
    twistd.linear.x = 0.0
    twistd.angular.z = 0.0
    pub.publish(twistd)
    
    # Publica el mensaje de Twist en el topic "/turtle1/cmd_vel"
    pub.publish(twist)
    rospy.sleep(5)
    # Espera hasta el próximo ciclo de publicación
        
    pub.publish(twistd)

    rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass