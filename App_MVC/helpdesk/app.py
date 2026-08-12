from flask import Flask, url_for, request, redirect, jsonify #type: ignore
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "Helpdesk026"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///helpdesk.db'

db.init_app(app)
