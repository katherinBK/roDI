from flask import Flask, request, jsonify
from rodi_py import RoDI

app = Flask(__name__)

rodi = None #almacenar a roDI en una instancia global

#ruta definida para conectaar a roDI
@app.route('/conectar', methods=['POST'])
def conectar():
  global rodi
  data = request.get_json()
  ip = data['ip']
  port = 1234  # Puerto fijo

  try:
    rodi = RoDI(ip=ip, port=port)
    return jsonify({'message': 'Conectado a RoDI!'})
  except Exception as e:
    return jsonify({'error': str(e)}), 500

'''if __name__ == '__main__':
  app.run(debug=True)''' 
