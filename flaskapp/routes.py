from flaskapp import app, mysql
from flask import render_template

@app.route('/')
def index():
       cursor = mysql.connection.cursor()
       cursor.execute("SELECT * FROM products") 
       products = cursor.fetchall()
       print(products)
       cursor.close()
       return render_template('index.html', products=products)