from flask import Flask, request, jsonify
import random
import rodi  # importar rodi

app = Flask(__name__)

# Simulación de la clase de control del robot (RoDI)
class RodiControl:
    def __init__(self):
        self.state = "stopped"
    
    def move_forward(self):
        self.state = "forward"
        return "RoDI moving forward"
    
    def move_backward(self):
        self.state = "backward"
        return "RoDI moving backward"
    
    def turn_left(self):
        self.state = "left"
        return "RoDI turning left"
    
    def turn_right(self):
        self.state = "right"
        return "RoDI turning right"
    
    def stop(self):
        self.state = "stopped"
        return "RoDI stopped"
    
    def get_distance(self):
       
        return random.uniform(10, 100)  
    
    def get_line_sensor(self):
        
        return random.choice(["Linea Detectada", "No Linea Detectada"])  

# Crear una instancia del controlador del robot
rodi = RodiControl()


@app.route('/control', methods=['POST'])
def control_rodi():
    command = request.json.get('command')
    
    if command == 'forward':
        response = rodi.move_forward()
    elif command == 'backward':
        response = rodi.move_backward()
    elif command == 'left':
        response = rodi.turn_left()
    elif command == 'right':
        response = rodi.turn_right()
    elif command == 'stop':
        response = rodi.stop()
    else:
        return jsonify({"error": "Comando desconocido"}), 400

    return jsonify({"message": response})


@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    sensor_type = request.args.get('type')
    
    if sensor_type == 'distancia':
        data = rodi.get_distance()
    elif sensor_type == 'linea':
        data = rodi.get_line_sensor()
    else:
        return jsonify({"error": "Tipo de sensor desconocido"}), 400

    return jsonify({"sensor": sensor_type, "data": data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
