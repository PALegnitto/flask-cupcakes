"""Flask app for Cupcakes"""

from flask import Flask, redirect, render_template, flash, jsonify, request
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

@app.get("/")
def homepage():

    return render_template("index.html")

@app.get("/api/cupcakes")
def get_all_cupcakes():
    """ Return JSON {cupcakes: [{id, flavor, size, rating, image}, ...]} """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """ Return JSON {cupcake: {id, flavor, size, rating, image}} """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post("/api/cupcakes")
def create_cupcake():
    """ Create cupcake from form data & return it.
    Return JSON {cupcake: {id, flavor, size, rating, image}} """

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    new_cupcake = Cupcake(flavor=flavor,
                        size=size,
                        rating=rating,
                        image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)

    ############### Updating and Deleting#################

@app.patch("/api/cupcakes/<int:cupcake_id>")
def update_cupcake_value(cupcake_id):
    """Updating individual values of a specific cupcake
    Return JSON {cupcake: {id, flavor, size, rating, image}} """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)

    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.delete("/api/cupcakes/<int:cupcake_id>")
def delete_cupcake(cupcake_id):
    """Deleting a specific cupcake
        Return JSON {deleted: cupcake_id} """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    # flash("Cupcake deleted!")

    message = {"deleted": cupcake_id}

    return jsonify(message)


