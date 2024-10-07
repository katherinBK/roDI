import rodi
import time

# Crear una instancia del robot RoDi
robot = rodi.RoDi()

# Función para detectar y evitar obstáculos
def detecta_obstáculos():
    while True:
        # Distancia del sensor de proximidad 
        distance = robot.get_distance()
        
        # Si el objeto está a menos de 5 cm, evitar el obstáculo
        if distance <= 5:
            print("objeto detectado"
            robot.move_backward(1)  # El robot se mueve hacia atrás 
            robot.move_left(1)  #El robot se mueve a la izquierda 
            time.sleep(1)  # Esperar 1 segundo
        else:
            # Si no hay ningún obstáculo, continuar
            robot.move_forward(1)
            time.sleep(1)
