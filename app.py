from flask import Flask, render_template, jsonify
from rodi import RoDI

app = Flask(__name__)
robot = RoDI(ip='192.168.4.1', port='1234')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control/<action>', methods=['POST'])
def control_robot(action):
    if action == "forward":
        robot.move_forward()
    elif action == "backward":
        robot.move_backward()
    elif action == "left":
        robot.move_left()
    elif action == "right":
        robot.move_right()
    elif action == "stop":
        robot.move_stop()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

