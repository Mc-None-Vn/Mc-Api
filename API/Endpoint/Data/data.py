from fastapi import APIRouter, Response, HTTPException
import requests

app = Flask(__name__)
url = "https://example.com/api/data"
data = {"name": "Name", "pw": "12345678"}

@app.route('/api/data/save', methods=['POST'])
def save_data():
    data = request.get_json()
    # Xử lý dữ liệu và lưu trữ vào cơ sở dữ liệu
    #...
    return jsonify({'message': 'Data has been saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Data has been saved successfully")
else:
    print("Error saving data")
