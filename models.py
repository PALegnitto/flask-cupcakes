"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cupcake(db.Model):
    """Cupcake"""

    # TODO: check that it is ok to use string here or if tbhey actually want text
    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)

    flavor = db.Column(db.String(25),
                    nullable = False)

    size = db.Column(db.String(25),
                            nullable = False)

    rating = db.Column(db.Integer,
                            nullable = False)

    image = db.Column(db.Text,
                            nullable = False,
                            default = "https://tinyurl.com/demo-cupcake")

    def serialize(self):
        """Serialize to dictionary"""

        return {
            "id": self.id,
            "name": self.name,
            "calories": self.calories
        }
