from flask import Flask, request, jsonify

app = Flask(__name__)

heart = [
    {
        "heart_id": "0",
        "date": "12/21/2023",
        "heart_rate": "78bpm",
    },
        {
        "heart_id": "1",
        "date": "12/24/2023",
        "heart_rate": "100bpm",
    },
    
]

#1. Create a REST API using FLASK insert a new heart record to a JSON file. The heart rate information is composed of heart_id, date and heart_rate.  (2 points)
@app.route('/heart', methods=['POST'])
def insert_new_heart():
    new_record = request.get_json()
    heart.append(new_record)
    return {'heart_id': len(heart)-1}, 200

#2, Create a REST API using FLASK to read a heart information from a JSON file. The heart rate information is composed of heart_id, date and heart_rate. (2 points)
@app.route('/heart', methods=['GET'])
def read_heart():
    return jsonify(heart)

#3. Create a REST API using FLASK to read a heart information of a specific heart_id from a JSON file. The heart rate information is composed of heart_id, date and heart_rate. (2 points)
@app.route('/heart/<int:index>', methods=['GET'])
def read_heart_id(index):
    specific = heart[index]
    return jsonify(specific)

#4. Create a REST API using FLASK to update a heart record of a specific heart_id. The heart rate information is composed of heart_id, date and heart_rate.  (2 points)
@app.route('/heart/<int:index>', methods=['POST'])
def update_heart_id(index):
    update_record = request.get_json()
    heart[index] = update_record
    return {'heart_id': len(heart)}, 200

#5. Create a REST API using FLASK to delete a heart record of a specific heart_id. The heart rate information is composed of heart_id, date and heart_rate.  (2 points).

@app.route('/heart/<int:index>', methods=['DELETE'])
def delete_heart_id(index):
    heart.pop(index)
    return 'A record has been deleted', 200


if __name__ == "__main__":
    app.run()