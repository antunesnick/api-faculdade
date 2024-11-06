from flask import Blueprint, Flask
from flask_restx import Api

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/doc', title='MasterGamers')
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mastergamers.db'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['CORS_HEADERS'] = 'Content-Type'
        self.player_ns = self.player_ns()


    def player_ns(self):
        return self.api.namespace(name='Player', description='player related operations', path='/')


    def run(self):
        self.app.run(
            port=5000,
            debug=True,
            host='localhost'
        )


server = Server()