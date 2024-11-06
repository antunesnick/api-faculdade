from db import db

class PlayerModel(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(127), nullable=False)
    email = db.Column(db.String(127), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    nickname= db.Column(db.String(127), nullable=False, unique=True)
    password= db.Column(db.String(63), nullable=False)
    game = db.Column(db.String(4), nullable=False)

    def __init__(self, name, email, age, nickname, password, game):
        self.name = name
        self.email = email
        self.age = age
        self.nickname = nickname
        self.password = password
        self.game = game

    def __repr__(self):
        return f'Name: {self.name}, Email: {self.email}, Nickname: {self.nickname}'
    
    def json(self):
        return{
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'nickname': self.nickname,
            'game': self.game
        }
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_nickname(cls, nickname):
        return cls.query.filter_by(nickname=nickname).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
        

   
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

        
