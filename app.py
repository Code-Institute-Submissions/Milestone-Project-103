import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'MilestoneProjectThree'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.Recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
        categories=mongo.db.Categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():

    ingredientslist = request.form.getlist('ingredients[]')
    if "" in ingredientslist:
        ingredientslist.remove("")
    methodslist = request.form.getlist('methods[]')
    if "" in methodslist:
        methodslist.remove("")

    recipes = mongo.db.Recipes
    recipe_name = request.form['recipe_name']
    yields = request.form['yield']
    category_name = request.form['category_name']
    equipment = request.form['equipment']
    ingredients = ingredientslist
    methods = methodslist
    image = request.form['image']

    recipe_data = {
        'recipe_name' : recipe_name,
        'yield' : yields,
        'category_name' : category_name,
        'equipment' : equipment,
        'ingredients' : ingredients,
        'methods' : methods,
        'image' : image
    }
    recipes.insert_one(recipe_data)
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.Categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.Recipes

    ingredientslist = request.form.getlist('ingredients[]')
    if "" in ingredientslist:
        ingredientslist.remove("")
    methodslist = request.form.getlist('methods[]')
    if "" in methodslist:
        methodslist.remove("")
    recipe_name = request.form['recipe_name']
    yields = request.form['yield']
    category_name = request.form['category_name']
    equipment = request.form['equipment']
    ingredients = ingredientslist
    methods = methodslist
    image = request.form['image']


    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name' : recipe_name,
        'yield' : yields,
        'category_name' : category_name,
        'equipment' : equipment,
        'ingredients' : ingredients,
        'methods' : methods,
        'image' : image
    })
    return redirect(url_for('get_recipes'))

""" @app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.Recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'category_name': request.form.get('category_name'),
        'yield': request.form.get('yield'),
        'equipment': request.form.get('equipment'),
        'ingredients': request.form.getlist('ingredients'),
        'image': request.form.get('image')
    })
    return redirect(url_for('get_recipes')) """


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.Recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=mongo.db.Categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

