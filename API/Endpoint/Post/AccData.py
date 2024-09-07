from flask import Flask, request, jsonify

app = Flask(__name__)
data = {}

@app.route('/api/post/acc/data', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_id = user_data['user_id']
    data[user_id] = user_data
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/post/acc/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in data:
        return jsonify(data[user_id]), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/api/post/acc/<user_id>', methods=['PATCH'])
def update_user(user_id):
    user_data = request.get_json()
    if user_id in data:
        data[user_id].update(user_data)
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404
