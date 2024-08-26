from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data/save', methods=['POST'])
def save_data():
    data = request.get_json()
    # Xử lý dữ liệu và lưu trữ vào cơ sở dữ liệu
    #...
    return jsonify({'message': 'Data has been saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)
