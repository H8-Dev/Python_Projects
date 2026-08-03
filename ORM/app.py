from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

app = Flask(__name__)
app.config['SECRET_KEY'] = "ABCPizzaria066"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzaria.db'
db = SQLAlchemy(app)

class TamanhoPizza(Enum):
    Broto = "20cm"
    Pequeno = "25cm"
    Medio = "30cm"
    Grande = "35cm"
    Gigante = "45cm"



class Pizzaria(db.Model):
    __tablename__ = 'pizzaria'
    uid = db.Column(db.Interger, primary_key=True),
    nome = db.Column(db.String(50), unique=True, nullable=False),
    sabor = db.Column(db.String(50), nullable=False),
    tamanho = db.Column(db.Enum(TamanhoPizza), nullable=False),
    entrega = db.Column(db.String(3), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def historico():
    pedidos = Pizzaria.query.all()
    return render_template('index.html', pedidos = pedidos)

@app.route('/insert', methods=['GET','POST'])
def fazer_pedido():
    if request.method == 'GET':
        return render_template('insert.html')
    else:
        pizza = Pizzaria(
            nome = request.form['nome'],
            sabor = request.form['sabor'],
            tamanho = request.form['tamanho'],
            entrega = request.form['entrega']
        )
        db.session.add(pizza)
        db.session.commit()
        return redirect(url_for(historico))

if __name__ == '__main__':
    app.run(debug=True)
