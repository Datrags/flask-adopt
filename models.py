from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEF_IMG = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmir-s3-cdn-cf.behance.net%2Fproject_modules%2Fmax_1200%2Fe8e97138267389.576411be19611.png&f=1&nofb=1&ipt=ff063e8f5bb4a2037b60047a5a1edebd2137ef652e1f6385d2321d9f4a1bf4ea&ipo=images"
class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    name = db.Column(db.Text, 
                     nullable=False)
    species = db.Column(db.Text, 
                        nullable=False)
    photo_url = db.Column(db.Text, 
                          nullable=False,
                          default=DEF_IMG)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available =db.Column(db.Boolean, 
                         nullable=False, 
                         default=True)