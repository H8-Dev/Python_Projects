from flask import Flask #type: ignore
from database import db
from dispositivo.disp_routes import disp_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'disp999'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventario.db'

db.init_app(app)
app.register_blueprint(disp_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)