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


@app.get("/api/cupcakes")
def get_all_cupcakes():
    """ Return JOSN {cupcakes: [{id, flavor, size, rating, image}, ...]} """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """ Return JOSN {cupcake: [{id, flavor, size, rating, image}]} """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post("/api/cupcakes")
def create_cupcake():
    """ Create cupcake from form data & return it.
    Return JOSN {cupcake: [{id, flavor, size, rating, image}]} """

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


