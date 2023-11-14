from flask import Flask, render_template, request, redirect, flash, url_for, make_response
import pymongo
from bson import json_util
import string
import random

mongo_client = pymongo.MongoClient("mongodb://admin:admin@mongodb:27017", connect=False)
db = mongo_client['recipes']
recipes_collections = db['recipes']

basic_recepts = [
  { "name": "Rohlik v parku", "author": "Ctirad", "description": "Dam rohlik do parku a ohreju v mikrovlnne troube.", "secret": "1234"},
  { "name": "Parek na sucho", "author": "Josefina", "description": "Dam si parek jen tak.", "secret": "parek"},
  { "name": "Omlaceny rohlik", "author": "Vlastislav", "description": "Omlatim rohlik nekomu o hlavu a snim to", "secret": "omlatit"},
  { "name": "Rohlik s colou", "author": "Melichar", "description": "Rohlik namocim v kole a snim to", "secret": "cocacola"},
  { "name": "Rohlik namazany chlebem", "author": "Jaromir", "description": "Nadrobim chleba na rohlik a rozprostru drobky podel rohliku", "secret": "chleb"},
  { "name": "Parek namazeny rohlikem", "author": "Borivoj", "description": "Udelam z rohliku neco jako pastiku a natru tim parek.", "secret": "rohlik"},
  { "name": "Chleba v parku v rohliku", "author": "Svatomil", "description": "Narvu rohlik do parku a takovou hmotu narvu do chleba. Snim to.", "secret": "nevim"},
]
recipes_collections.insert_many(basic_recepts)

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/recipes')
def recipes():
    recipes_list = recipes_collections.find()
    return render_template('recipes.html', recipes=recipes_list)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        description = request.form['description']
        secret = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, 8))
        record = {'name': name, 'author': author, 'description': description, "secret": secret}
        recipes_collections.insert_one(record)

        # flash success and redirect to form
        flash(f'Your recipe has been added! Your secret is {secret}')
        return redirect(url_for('form'))
    else:
        return render_template('form.html')


@app.route('/api/recipe', methods=['POST'])
def api_post_recipe():
    name = request.args.get('name')
    author = request.args.get('author')
    description = request.args.get('description')
    secret = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, 8))
    record = {'name': name, 'author': author, 'description': description, "secret": secret}
    if recipes_collections.find_one({'name': name, "author": author}) == None:
        recipes_collections.insert_one(record)
        return make_response(json_util.dumps({'success': 'Recipe added', "secret": secret}), 200)
    else:
        return make_response(json_util.dumps({'error': 'Recipe already exists'}), 400)
    

@app.route('/api/recipes')
def api_get_recipes():
    recipes_list = recipes_collections.find({}, {"_id": 0, "secret": 0})
    return make_response(json_util.dumps(recipes_list), 200)


@app.route('/api/recipe')
def api_get_recipe():
    name = request.args.get('name')
    author = request.args.get('author')
    recipe = recipes_collections.find_one({'name': name, "author": author},  {"_id": 0, "secret": 0})
    if recipe:
        return make_response(json_util.dumps(recipe), 200)
    else:
        return make_response(json_util.dumps({'error': 'Recipe not found'}), 404)
    

@app.route('/api/recipe', methods=['PUT'])
def api_put_recipe():
    name = request.args.get('name')
    author = request.args.get('author')
    description = request.args.get('description')
    secret = request.args.get('secret')
    if recipes_collections.find_one({'name': name, "author": author, "secret": secret}):
        recipes_collections.update_one({'name': name, "author": author, "secret": secret}, {"$set": {"description": description}})
        return make_response(json_util.dumps({'success': 'Recipe updated'}), 200)
    else:
        return make_response(json_util.dumps({'error': 'Recipe not found'}), 404)


@app.route('/api/recipe', methods=['DELETE'])
def api_delete_recipe():
    name = request.args.get('name')
    author = request.args.get('author')
    secret = request.args.get('secret')
    if recipes_collections.find_one({'name': name, "author": author, "secret": secret}):
        recipes_collections.delete_one({'name': name, "author": author, "secret": secret})
        return make_response(json_util.dumps({'success': 'Recipe deleted'}), 200)
    else:
        return make_response(json_util.dumps({'error': 'Recipe not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)



