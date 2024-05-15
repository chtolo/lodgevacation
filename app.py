from flask import Flask, render_template, request, flash, redirect, url_for

from pymongo import MongoClient

app = Flask(__name__, static_folder='assets')

# Connexion à la base de données MongoDB
client = MongoClient('localhost', 27017)
db = client['My_DB']
users_collection = db['utilisateurs']

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about",methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route("/contact",methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route("/houses", methods=['GET', 'POST'])
def houses():
    return render_template('houses.html')
@app.route("/services",methods=['GET', 'POST'])
def services():
    return render_template('services.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Vérifier si l'utilisateur existe dans la base de données
        user = users_collection.find_one({'email': email, 'password': password})
        if user:
            # Utilisateur trouvé, rediriger vers la page de profil
            return redirect(url_for('profile'))
        else:
            # Utilisateur non trouvé, afficher un message d'erreur
            flash('Identifiants incorrects. Veuillez réessayer.', 'error')
    return render_template('login.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # Vérifier si l'utilisateur existe déjà dans la base de données
        existing_user = users_collection.find_one({'email': email})
        if existing_user:
            # Utilisateur existant, afficher un message d'erreur
            flash('Cet email est déjà utilisé. Veuillez utiliser un autre email.', 'error')
        else:
            # Ajouter l'utilisateur à la base de données
            new_user = {'name': name, 'email': email, 'password': password}
            users_collection.insert_one(new_user)
            return redirect(url_for('profile'))
    return render_template('signup.html')

@app.route("/profile")
def profile():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    user_info = {'username': name, 'email': email ,'password': password }
    return render_template('profile.html', user=user_info)

if __name__ == '__main__':
	app.run(debug = True)