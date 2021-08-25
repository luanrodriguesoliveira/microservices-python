from enum import unique
from pony.orm import *
from pony.orm.serialization import to_dict

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

class Theater(db.Entity):         
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    seats = Set("Seat")
    
class Seat(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    is_available = Required(bool)
    theater = Required(Theater)

db.generate_mapping(create_tables=True)

@db_session()
def save_theater(body):
    Theater(name=body['name'])

@db_session()
def save_seat(theater_id, body):
    theater = Theater[theater_id]
    Seat(name=body['name'], is_available=body['isAvailable'], theater=theater)

@db_session()
def find_all_theaters():
    theaters = select(m for m in Theater)[:]
    result = [m.to_dict() for m in theaters]
    return result

@db_session()
def find_seats_by_theater(theater_id):
    theater = Theater[theater_id]
    seats = select(s for s in Seat if s.theater == theater)[:]
    result = [s.to_dict() for s in seats]
    return result

# def occupy_seat