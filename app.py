"""Flask app for Cupcakes"""

from flask import Flask, redirect, render_template, flash, jsonify


from models import Cupcake, db, connect_db, Playlist, Song, PlaylistSong

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"



@app.get("/api/cupcakes")
def get_all_cupcakes():
    """ Return JOSN {cupcakes: [{id, flavor, size, rating, image}, ...]} """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

