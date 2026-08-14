from flask import Flask #type: ignore
from database import db
from routers.routes import user_bp, chamado_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = "Helpdesk026"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///helpdesk.db'

db.init_app(app)

app.register_blueprint(user_bp)
app.register_blueprint(chamado_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)