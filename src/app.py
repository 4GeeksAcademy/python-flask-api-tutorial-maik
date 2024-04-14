from flask import Flask, jsonify
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():




    # Puedes convertir esa variable en una cadena json de la siguiente manera
    json_text = jsonify(todos)

    # Y luego puedes devolverlo al front-end en el cuerpo de la respuesta de la siguiente manera
    return json_text


# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)