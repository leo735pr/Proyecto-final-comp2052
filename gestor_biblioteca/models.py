from app import db
from flask_login import UserMixin

# Tabla de roles (por ejemplo: administrador, lector, bibliotecario)
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Tabla de usuarios
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

# Tabla de libros
class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    autor = db.Column(db.String(150), nullable=False)
    categoria = db.Column(db.String(100))
    anio = db.Column(db.Integer)
    descripcion = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
