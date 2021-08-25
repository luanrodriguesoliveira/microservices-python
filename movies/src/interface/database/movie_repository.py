from pony.orm import *
from pony.orm.serialization import to_dict

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


class Movie(db.Entity):         
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    description = Required(str)
    imgUri = Required(str)

db.generate_mapping(create_tables=True)

@db_session()
def save_movie(body):
    Movie(name=body['name'], description=body['description'], imgUri=body['imgUri'])

@db_session()
def find_all_movies():
    movies = select(m for m in Movie)[:]
    result = [m.to_dict() for m in movies]
    return result

@db_session()
def find_movie_by_id(id):
    movie = Movie[id]
    return movie

@db_session()
def update_movie(id, body):
    movie = Movie[id]
    movie.set(name=body['name'], description=body['description'], imgUri=body['imgUri'])

@db_session()
def delete_movie(id):
    movie = Movie[id]
    movie.delete()