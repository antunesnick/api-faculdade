from flask import jsonify
from marshmallow import ValidationError
from flask_cors import CORS, cross_origin

from db import db
from ma import ma
from controllers.player import Player, PlayerList

from server.instance import server


api = server.api
app = server.app

CORS(app)


def create_tables():
    with app.app_context():
        db.create_all()

api.add_resource(Player, '/players/<int:id>')
api.add_resource(PlayerList, '/players')



if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()

