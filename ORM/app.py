from flask import Flask, render_template, url_for, request, redirect
from database import db
from enum import Enum

app = Flask(__name__)
app.config['SECRET_KEY'] = "ABCPizzaria066"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzaria.db'

db.init_app(app)

class TamanhoPizza(Enum):
    Broto = "20cm"
    Pequeno = "25cm"
    Medio = "30cm"
    Grande = "35cm"
    Gigante = "45cm"



class Pizzaria(db.Model):
    __tablename__ = 'pizzaria'
    
    uid = db.Column(db.Integer, primary_key=True),
    nome = db.Column(db.String(50), unique=True, nullable=False),
    sabor = db.Column(db.String(50), nullable=False),
    tamanho = db.Column(db.Enum(TamanhoPizza), nullable=False),
    preco = db.Column(db.Float(precision=2))
    entrega = db.Column(db.String(3), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/pedidos')
def historico():
    pedidos = Pizzaria.query.all()
    return render_template('historico.html', pedidos = pedidos)

@app.route('/pedidos/insert', methods=['GET','POST'])
def fazer_pedido():
    if request.method == 'GET':
        return render_template('insert.html')
    else:
        try:
            pizza = Pizzaria(
                nome = request.form['nome'],
                sabor = request.form['sabor'],
                tamanho = tamanho_check,
                preco = request.form['preco'],
                entrega = request.form['entrega']
            )
            db.session.add(pizza)
            db.session.commit()
            return redirect(url_for(historico))

        except SQLAlchemyError:
            db.session.rollback()
            return jsonify({"erro": "Erro ao salvar o pedido no banco de dados"})

@app.route('/pedidos/concluir', methods=['POST'])
def concluir_pedido():
    return jsonify("Função não disponível no momento.")


if __name__ == '__main__':
    app.run(debug=True)
