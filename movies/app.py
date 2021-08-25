import os
from flask import Flask, jsonify, request
from pony.orm.serialization import to_dict, json
from src.interface.database import movie_repository
app = Flask(__name__)

@app.route('/movie', methods=['POST'])
def post_movie():
    try: 
        body = request.json
        movie_repository.save_movie(body)
        return jsonify({'status': 'created', 'body': body}), 201
    except:
        return jsonify({'status': 'error', 'message': 'oops, something wrong happened'}), 500

@app.route('/movie', methods=['GET'])
def get_all_movies(): 
    try:  
        movie = movie_repository.find_all_movies()   
        return jsonify(movie), 200
    except:
        return jsonify({'status': 'error', 'message': 'oops, something wrong happened'}), 500

@app.route('/movie/<movie_id>', methods=['GET'])
def get_movie(movie_id): 
    try:  
        movie = movie_repository.find_movie_by_id(movie_id)
        return jsonify(movie.to_dict()), 200
    except:
        return jsonify({'status': 'error', 'message': 'oops, something wrong happened'}), 500

@app.route('/movie/<movie_id>', methods=['PUT'])
def put_movie(movie_id):
    try:
        body = request.json
        movie_repository.update_movie(movie_id, body)
        return jsonify({'status': 'ok', 'body': body}), 200
    except:
        return jsonify({'status': 'error', 'message': 'oops, something wrong happened'}), 500

@app.route('/movie/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):   
    try:
        movie_repository.delete_movie(movie_id)
        return jsonify({'status': 'ok'}), 200
    except:
        return jsonify({'status': 'error', 'message': 'oops, something wrong happened'}), 500


if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
