import os
from flask import Flask, jsonify, request
from pony.orm.core import ExprEvalError
from pony.orm.serialization import to_dict, json
from src.interface.database import theater_repository
app = Flask(__name__)

@app.route('/theater', methods=['POST'])
def post_theater():
    try: 
        body = request.json
        theater_repository.save_theater(body)
        return jsonify({'status': 'created', 'body': body}), 201
    except:
        return jsonify({'status': 'error', 'message': 'oops, something wrong happened'}), 500

@app.route('/theater/<theater_id>/seat', methods=['POST'])
def post_seat(theater_id):
    try: 
        body = request.json
        theater_repository.save_seat(theater_id, body)
        return jsonify({'status': 'created', 'body': body}), 201
    except:
        return jsonify({'status': 'error', 'message': 'oops, something wrong happened'}), 500

@app.route('/theater', methods=['GET'])
def get_all_theaters():
    try:  
        movie = theater_repository.find_all_theaters() 
        return jsonify(movie), 200
    except:
        return jsonify({'status': 'error', 'message': 'oops, something wrong happened'}), 500

@app.route('/theater/<theater_id>/seat', methods=['GET'])
def get_seats_by_theater(theater_id): 
    try:  
        seats = theater_repository.find_seats_by_theater(theater_id)
        return jsonify(seats), 200
    except:
        return jsonify({'status': 'error', 'message': 'oops, something wrong happened'}), 500

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
