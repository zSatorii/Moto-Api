from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

peritajes_db = []

@app.route('/api/repuestos')
def get_repuestos():
	return jsonify({
	  "status" : "Online",
	  "servidor" : "Ubuntu de Castro",
	  "hora_servidor" : str(datetime.datetime.now()),
	  "inventario" : ["Bujias de Iridio", "Filtro de aceite", "Aceite motul 7100"]
	})

@app.route('/api/peritajes', methods=['POST'])
def crear_peritaje():
	datos = request.get_json()

	nuevo_peritaje = {
	 "placa": datos['placa'].upper(),
 	 "fecha_registro": str(datetime.datetime.now())
	}

	peritajes_db.append(nuevo_peritaje)

	return jsonify({
	  "mensajes": "Peritaje creado",
	  "peritaje": nuevo_peritaje
	}), 201

@app.route('/api/peritajes', methods=['GET'])
def obtener_peritajes():
	return jsonify({
	 "status":"Online",
	 "total_registros":len(peritajes_db),
	 "peritajes": peritajes_db
	})



if __name__ == "__main__":
	app.run()
