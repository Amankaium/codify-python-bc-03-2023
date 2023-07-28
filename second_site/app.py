from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/cars"
db.init_app(app)


class CarsUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=True)
    workers_count = db.Column(db.Integer, default=0)

@app.route("/")
def homepage():
    return render_template('home.html')

@app.route('/user/<int:id>')  # user/2/
def user_info(id):  # id = 2
    user_object = db.get_or_404(CarsUser, id)  # SELECT * FROM cars_user WHERE id=2
    return render_template('detail.html', user=user_object)

@app.route("/users")
def user_list():
    users = db.session.execute(db.select(CarsUser)).scalars()
    return render_template("list.html", users=users)

@app.route('/shops')
def shops():
    shops_query = db.session.execute(db.select(Shop)).scalars()
    students = ['Aisana', 'Aidana', 'Ivan', 'Davlyat']
    return render_template(
        'shops_list.html',
        shops_list=shops_query,
        students_list=students
    )

@app.route('/shop/<int:id>/')
def shop_detail(id):
    shop = db.get_or_404(Shop, id)
    return render_template(
        'shop_detail.html',
        shop_object=shop
    )

with app.app_context():
    db.create_all()
