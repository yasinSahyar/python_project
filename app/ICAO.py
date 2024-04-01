from flask import Flask, jsonify

app = Flask(__name__)

# Define a dictionary to store airport information (replace this with your own airport database)
airport_db = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "Heathrow Airport", "Location": "London"},
    # Add more airport entries as needed
}

@app.route('/airport/<string:icao>', methods=['GET'])
def get_airport_info(icao):
    if icao in airport_db:
        airport_info = {"ICAO": icao, **airport_db[icao]}
        return jsonify(airport_info)
    else:
        return jsonify({"error": "ICAO code not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
