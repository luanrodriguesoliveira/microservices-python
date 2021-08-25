from pony.orm import *
db = Database()

class Movie(db.Entity): 
        
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    description = Required(str)
    imgUri = Required(str)

