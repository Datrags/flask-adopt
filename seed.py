from models import Pet, db
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    Pet.query.delete()

    fonzi = Pet(name="Fonzi", species="dog", available=False, age=17)
    kaz = Pet(name="Kaz", species="dog", age=12)
    felix = Pet(name="Felix", species="cat", age=50)
    sonic = Pet(name="Sonic", species="Hedgehog", 
                age=32, 
                available=False, 
                photo_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.6X7mgSMxsJ1W5SQOUY24ywHaLk%26pid%3DApi&f=1&ipt=ba1222c74f173c9315de990e1ac4337b4565ff5374ab24c36917cf7a7193a035&ipo=images")

    db.session.add(fonzi)
    db.session.add(kaz)
    db.session.add(felix)
    db.session.add(sonic)

    db.session.commit()
