
# crud backend (create, read, update delete)

# different end routes for the API

# create
# first_name, last_name, email
# request is anything we send to the server. GET, POST, PATCH, DELETE and pther requests. 

from flask import request, jsonify
from config import app, db
from models import Contact


# simple get method

@app.route("/contacts", methods=["GET"])
# end request of contacts
def get_contacts():
    contacts = Contact.query.all()
    # gives the list of all contacts
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    # taking all the elements from contacts and then applying to_json
    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    
    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name and email"}),
            400,
        )
        
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact) # add it to the db and is in staging area
        db.session.commit() # then commit and add it to the database
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "user created!"}), 201

@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id) # find the contact with the user id
    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    #looking for data inside the request. If there is a new name, update contact first name.
    # otherwise leave it the way it was.
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)
    
    db.session.commit() # commit the changes 
    
    return jsonify({"message": "contact updated."}), 200
    
     
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()
    
    return jsonify({"message": "user deleted!"}), 200


if __name__ == "__main__":
    # instantiate db
    
    with app.app_context():
        db.create_all() # create all of the different models that we have defined on the db
        
    
    app.run(debug=True)


