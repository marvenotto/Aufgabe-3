from flask import Flask, request, jsonify

app = Flask(__name__)

persons = {}

@app.route('/person', methods=['POST'])
def create_person():
    data = request.get_json()
    name = data.get('name')
    if name in persons:
        return jsonify({'error': 'Person already exists'}), 400
    persons[name] = data
    return jsonify({'message': 'Person created'}), 201

@app.route('/person/<name>', methods=['PUT'])
def update_person(name):
    data = request.get_json()
    if name not in persons:
        return jsonify({'error': 'Person not found'}), 404
    persons[name].update(data)
    return jsonify({'message': 'Person updated'}), 200

@app.route('/person/<name>', methods=['GET'])
def get_person(name):
    if name not in persons:
        return jsonify({'error': 'Person not found'}), 404
    return jsonify(persons[name]), 200

@app.route('/person/<name>', methods=['DELETE'])
def delete_person(name):
    if name not in persons:
        return jsonify({'error': 'Person not found'}), 404
    del persons[name]
    return jsonify({'message': 'Person deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
