# database models

from config import db  
# instance which will give instance of the db created

class Contact(db.Model):
    # database model represneted as a python class.
    # different field this db have
    
    id = db.Column(db.Integer, primary_key=True)
    # This is the key we are going to index this and must be unique for every entry.
    
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    # pass first name, maximum string length of 80. 
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def to_json(self):
        # convert all the fields above to dictionary. 
        # convert into json. Communicate using json format. 
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
        
    
    
    

    
