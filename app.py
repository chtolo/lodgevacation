from flask import Flask, flash, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder='assets')

# Configuration de la base de données MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)

app.secret_key = 'your_secret_key'  # Définissez une clé secrète unique et sécurisée

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route("/houses", methods=['GET', 'POST'])
def houses():
    return render_template('houses.html')

@app.route("/marrakech_details1", methods=['GET', 'POST'])
def marrakech_details1():
    return render_template('marrakech_details1.html')

@app.route("/marrakech_details2", methods=['GET', 'POST'])
def marrakech_details2():
    return render_template('marrakech_details2.html')

@app.route("/marrakech_details3", methods=['GET', 'POST'])
def marrakech_details3():
    return render_template('marrakech_details3.html')

@app.route("/agadir_details1", methods=['GET', 'POST'])
def agadir_details1():
    return render_template('agadir_details1.html')

@app.route("/agadir_details2", methods=['GET', 'POST'])
def agadir_details2():
    return render_template('agadir_details2.html')

@app.route("/agadir_details3", methods=['GET', 'POST'])
def agadir_details3():
    return render_template('agadir_details3.html')
@app.route('/reservation', methods=['POST'])




def reservation():
    if 'email' not in session:
        flash('Vous devez être connecté pour faire une réservation.', 'error')
        return redirect(url_for('login'))  # Redirigez vers la page de connexion

    email = session['email']

    # Vérifiez que les autres champs sont présents
    nom_maison = request.form.get('nomdemaison')
    date = request.form.get('date')
    nombre_personnes = request.form.get('nombrePersonnes')
    nombre_nuits = request.form.get('nombreNuits')

    if not nom_maison or not date or not nombre_personnes or not nombre_nuits:
        flash('Tous les champs sont requis.', 'error')
        return redirect(url_for('reservation_form_page'))  # 'reservation_form_page' est le nom de la route de votre formulaire de réservation

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM user WHERE email = %s', (email,))
    user = cur.fetchone()
    if not user:
        flash('Utilisateur non trouvé.', 'error')
        return redirect(url_for('reservation_form_page'))

    # Vérifiez si la maison est déjà réservée à la même date
    cur.execute('SELECT * FROM reservation WHERE nom_maison = %s AND date = %s', (nom_maison, date))
    existing_reservation = cur.fetchone()
    if existing_reservation:
        flash('Cette maison est déjà réservée pour cette date.', 'error')
        return 'cette maison est réservé pour cette date '

    # Insérer la réservation si elle n'existe pas déjà
    cur.execute("INSERT INTO reservation (email, nom_maison, date, nombre_personnes, nombre_nuits) VALUES (%s, %s, %s, %s, %s)", 
                (email, nom_maison, date, nombre_personnes, nombre_nuits))
    mysql.connection.commit()
    cur.close()
    
    return 'Réservation enregistrée avec succès !'

@app.route("/login", methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        user = cursor.fetchone()
        
        if user and check_password_hash(user['password'], password):
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            return redirect(url_for('profile'))
        else:
            message = 'Please enter correct email / password!'
    return render_template('login.html', message=message)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        account = cursor.fetchone()
        
        if account:
            message = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid email address!'
        elif not name or not password or not email:
            message = 'Please fill out the form!'
        else:
            hashed_password = generate_password_hash(password)
            cursor.execute('INSERT INTO user (name, email, password) VALUES (%s, %s, %s)', (name, email, hashed_password))
            mysql.connection.commit()
            message = 'You have successfully registered!'
    elif request.method == 'POST':
        message = 'Please fill out the form!'
    
    return render_template('signup.html', message=message)

@app.route("/profile")

def profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE userid = %s', (session['userid'],))
        user = cursor.fetchone()
        return render_template('profile.html', user=user)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)