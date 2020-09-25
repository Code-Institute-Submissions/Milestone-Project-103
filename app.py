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
@app.route('/find_recipe')
def find_recipe():
    """ Home page """
    recipes = list(mongo.db.Recipes.find())
    categories = mongo.db.Categories.find()
    return render_template('contents.html', recipes=recipes, categories=categories)


@app.route('/get_recipes')
def get_recipes():
    """ View all recipes """
    return render_template("recipes.html", recipes=mongo.db.Recipes.find())


@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    """ View an individual recipe """
    the_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.Categories.find()
    return render_template('singlerecipe.html', recipe=the_recipe, categories=all_categories)


@app.route('/add_recipe')
def add_recipe():
    """ Add a recipe """
    return render_template('addrecipe.html',
        categories=mongo.db.Categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    """ Insert the recipe to the database and redirect the user to the View all recipes page """
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
    """ Edit a recipe """
    the_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.Categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    """ Insert the edited recipe into the database and redirect the site user to the View all recipes page """
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

    recipes.update({'_id': ObjectId(recipe_id)},
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


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """ Delete a recipe and redirect the user to the View all recipes page """
    mongo.db.Recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


@app.route('/get_categories')
def get_categories():
    """ Retrieve all categories with a view to editing or deleting them """
    return render_template('categories.html',
    categories=mongo.db.Categories.find())


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    """ Edit a category """
    return render_template('editcategory.html', 
    category = mongo.db.Categories.find_one({'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=["POST"])
def update_category(category_id):
    """ Insert the updated category into the database and redirect the user to the categories list page """
    categories = mongo.db.Categories
    category_name = request.form['category_name']

    categories.update({'_id': ObjectId(category_id)},
    {
        'category_name' : category_name
    })
    return redirect(url_for('get_categories'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    """ Delete a category and redirect the user to the categories list page """
    mongo.db.Categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    """ Add a category """
    return render_template('addcategory.html')


@app.route('/insert_category', methods=['POST'])
def insert_category():
    """ Insert the new category into the database and redirect the user to the categories list page """
    category = mongo.db.Categories
    category_document = {'category_name': request.form.get('category_name')}
    category.insert_one(category_document)
    return redirect(url_for('get_categories'))


""" Run the application """
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)