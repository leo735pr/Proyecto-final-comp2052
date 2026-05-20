from flask import render_template, request, redirect, url_for
from app import db
from app.models import Libro
from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    libros = Libro.query.all()
    return render_template('index.html', libros=libros)

@routes.route('/agregar', methods=['POST'])
def agregar_libro():
    titulo = request.form['titulo']
    autor = request.form['autor']
    categoria = request.form['categoria']
    anio = request.form['anio']
    descripcion = request.form['descripcion']

    nuevo_libro = Libro(titulo=titulo, autor=autor, categoria=categoria, anio=anio, descripcion=descripcion)
    db.session.add(nuevo_libro)
    db.session.commit()

    return redirect(url_for('routes.index'))

@routes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_libro(id):
    libro = Libro.query.get_or_404(id)
    if request.method == 'POST':
        libro.titulo = request.form['titulo']
        libro.autor = request.form['autor']
        libro.categoria = request.form['categoria']
        libro.anio = request.form['anio']
        libro.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('routes.index'))
    return render_template('editar.html', libro=libro)

@routes.route('/eliminar/<int:id>')
def eliminar_libro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return redirect(url_for('routes.index'))
