from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def handle_todos():
    my_json = jsonify(todos)
    return my_json


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    response_body = todos
    return response_body


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]





# Estas dos líneas siempre seben estar al final de tu archivo app.py.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)