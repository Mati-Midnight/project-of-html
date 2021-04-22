from flask import Flask, render_template
from data import db_session
from data.news import News
from data.dish import Dish
from data.category import Category

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    news = db_sess.query(News)
    return render_template('main.html', news=news)


@app.route('/me')
def me():
    return render_template('me.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/first_dish')
def first_dish():
    dish = db_sess.query(Dish)
    return render_template('dishes.html', title='Первые блюда', dish=dish)


@app.route('/second_dish')
def second_dish():
    dish = db_sess.query(Dish)
    return render_template('dishes.html', title='Вторые блюда', dish=dish)


@app.route('/snacks')
def snacks():
    dish = db_sess.query(Dish)
    return render_template('dishes.html', title='Закуски', dish=dish)


@app.route('/salads')
def salads():
    dish = db_sess.query(Dish)
    return render_template('dishes.html', title='Салаты', dish=dish)


@app.route('/desserts')
def desserts():
    dish = db_sess.query(Dish)
    return render_template('dishes.html', title='Десерты', dish=dish)


@app.route('/bakery')
def bakery():
    dish = db_sess.query(Dish)
    return render_template('dishes.html', title='Выпечка', dish=dish)


@app.route('/cake')
def cake():
    dish = db_sess.query(Dish)
    return render_template('dishes.html', title='Торты', dish=dish)


@app.route('/sauces')
def sauces():
    dish = db_sess.query(Dish)
    return render_template('dishes.html', title='Соусы, кремы', dish=dish)


@app.route('/new_recipe')
def new_recipe():
    return render_template('new_rec.html')


if __name__ == '__main__':
    db_session.global_init("db/blog.sqlite")
    db_sess = db_session.create_session()
    app.run(port=1012, host='127.0.0.1')
