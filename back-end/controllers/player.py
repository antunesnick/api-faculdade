from flask import request
from flask_cors import cross_origin
from flask_restx import Resource, fields

from models.player import PlayerModel
from schemas.player import PlayerSchema

from server.instance import server

player_ns = server.player_ns

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)

item = player_ns.model('Player', {
        'name': fields.String(description= 'Player name'),
        'email':fields.String(description= 'Player e-mail') ,
        'age': fields.Integer(),
        'nickname': fields.String(description= 'Player Nickname'),
        'password': fields.String(description = 'Player Password'),
        'game': fields.String(description='Player selected game')
})



    

class Player(Resource):
    
    def get(self, id):
        player_data = PlayerModel.find_by_id(id)
        if player_data:
            return player_schema.dump(player_data), 200
        return "PLAYER NOT FOUND", 404
    
    @player_ns.expect(item)
    def put(self,id):
        player_data = PlayerModel.find_by_id(id)
        player_json = request.get_json()

        if player_json['email']:
            player_data.email = player_json['email']
        if player_json['age']:
            player_data.age = player_json['age']
        if player_json['nickname']:
            player_data.nickname = player_json['nickname']
        if player_json['game']:
            player_data.game = player_json['game']
        
        player_data.save_to_db()

        return player_schema.dump(player_data), 200


    def delete(self, id):
        player_data = PlayerModel.find_by_id(id)
        if player_data:
            player_data.delete_from_db()
            return f'PLAYER ID {id} SUCCESSFULLY DELETED', 200
        return "PLAYER NOT FOUND", 404
        



class PlayerList(Resource):

    def get(self):
        return players_schema.dump(PlayerModel.find_all())
    

    @player_ns.expect(item)
    @player_ns.doc('Create an item')
    def post(self):
        player_json = request.get_json()
        player_data = player_schema.load(player_json)
        player_data.save_to_db()


        return player_data.json(), 201
    
