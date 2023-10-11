from app import app
from flask import render_template, request
from .forms import pokemonform
from .utils import get_pokemon



@app.route("/")
def index_html():
    python_people = ["Shoha", "Pearl", "Jennifer", "Dimitrius", "Donte", "Brendan"]
    return render_template("index.html", message="Hello from my template", red=True, html_people=python_people)

@app.route("/new-html")
def new_html():
    return render_template("base.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/json")
def json():
    return {"message": "Hello from my updated API!"}


@app.route("/input",methods=["GET","POST"])
def input_pokemon():
    form = pokemonform()    
    if request.method == "POST":
        print("POST")
        print(form.pokemon.data)
        if form.validate():
            print("validate")
            query = form.pokemon.data
            pokemon = get_pokemon(query)
            print(pokemon)
            if pokemon: 
                return render_template('input.html', form=form, pokemon=pokemon)
    return render_template('input.html', form=form)
    


