from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL 
import mysql.connector

# line 8 initialize de programm, lines 10 to 14 contain the neccesary values to connect with the DB created usin MYSQL

application = Flask(__name__)

application.config['MYSQL_HOST'] = 'localhost' # define ruta para conectarse a la DB
application.config['MYSQL_USER'] = 'root' # define usuario para conectarse a la DB
application.config['MYSQL_PASSWORD'] = 'Spain&Japan1991*' # efine contraseña para conectarse a la DB
application.config['MYSQL_DB'] = 'flask_contacts' # define la DB a la cual debe conectarse la aplicación
mysql = MySQL(application)

application.secret_key = 'mysecretkey'

# This variable is the actual connection with the DB
database = MySQL()

# Main route to stablish a connection with localhost
@application.route('/')
def index():
    cur1 = mysql.connection.cursor()
    cur1.execute('SELECT * FROM contacts')
    showdata = cur1.fetchall()
    print(showdata) 
    return render_template('index.html', showcontacts = showdata)

@application.route('/add_contact', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
        names = request.form ['names']
        lastNames = request.form ['lastNames']
        phone = request.form ['phone']
        email = request.form ['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (names, lastnames, phone, email) VALUES (%s, %s, %s, %s)', (names, lastNames, phone, email))
        mysql.connection.commit()
        flash('Contact added successfully')
        return redirect(url_for('index'))

@application.route('/edit/<id>')
def edit_contact(id):
    editCur = mysql.connection.cursor()
    editCur.execute('SELECT * FROM contacts WHERE id = %s', [id])
    editData = editCur.fetchall() 
    return render_template ('edit_contact.html', showcontact = editData[0])

@application.route('/update/<id>', methods = ['post'])
def update_contact(id):
    if request.method == 'POST':
        names = request.form['names']
        lastNames = request.form['lastNames']
        phone = request.form['phone']
        email = request.form['email']
        updateCur = mysql.connection.cursor()
        updateCur.execute(""" 
        UPDATE contacts
        SET names = %s,
            lastNames = %s,
            phone = %s,
            email = %s
        WHERE id = %s 
        """, (names, lastNames, phone, email, id))
        mysql.connection.commit()
        flash('Contact successfully updated')
        return redirect(url_for('index'))

@application.route('/delete/<string:id>')
def delete_contact(id):
    deleteCur = mysql.connection.cursor()
    deleteCur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('contact successfully deleted')
    return redirect(url_for('index'))

if __name__ == '__main__':
    application.run(port = 3000, debug = True)
