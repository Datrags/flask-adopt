from flask import Flask, render_template, redirect, flash
from forms import AddPetForm
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"

with app.app_context():
    connect_db(app)
    db.create_all()

@app.route("/")
def home_page():
    """Starting page"""
    pets = Pet.query.all()
  
    return render_template('home.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form """

    form = AddPetForm()

    spec = list(set([(p.species, p.species) for p in Pet.query.all()]))
    print("printing spec",spec)
    form.species.choices = spec
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name,
                  species=species, 
                  photo_url=photo_url, 
                  age=age, 
                  notes=notes
                  )
        
        db.session.add(pet)
        db.session.commit()

        flash(f"Added a {species} named {name}!")
        return redirect("/add")
    else:
        #return spec
        return render_template("add_pet.html", form=form)

@app.route("/<int:id>", methods=["POST", "GET"])
def pet_page(id):
    """Pet view and edit form """

    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)
    # spec = db.session.query(Pet.species)
    # spec_list = list(set([(s, s) for s in spec]))
    # print("********************************")
    # print(spec_list, " SPEC LIST")
    spec = list(set([(p.species, p.species) for p in Pet.query.all()]))
    form.species.choices = spec
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        flash(f"Changes Successful to {pet.name}")

        db.session.add(pet)
        db.session.commit()
        return redirect(f"/{id}")
    else:
        return render_template("display.html", form=form, pet=pet)
