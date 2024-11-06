from ma import ma
from models.player import PlayerModel

class PlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PlayerModel
        load_instance = True
        