from flask import redirect, render_template, request, flash, session
from flask_crud.__init__ import app
from flask_crud.models.usuario import Usuario
from flask_crud.__init__ import bcrypt
import os

@app.route("/")
def login():

    if 'usuario_nombre' in session:
        flash('Ya estás LOGEADO!', 'warning')
        return redirect('/home')

    return render_template("login.html",number=0)

@app.route("/procesar_registro", methods=["POST"])
def procesar_registro():

    if not Usuario.validar(request.form):
        flash('Usuario no registrado','error')
        return redirect('/')

    pass_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'nombre' : request.form['nombre'],
        'apellido' : request.form['apellido'],
        'email' : request.form['email'],
        'password' : pass_hash,
    }

    resultado = Usuario.save(data)

    if not resultado:
        flash("error al crear el usuario", "error")
        return redirect("/")

    flash("Usuario creado correctamente", "success")
    return redirect("/")


@app.route("/procesar_login", methods=["POST"])
def procesar_login():

    usuario = Usuario.buscar(request.form['identificacion'])

    if not usuario:
        flash("Usuario/Correo/Clave Invalidas", "error")
        return redirect("/")

    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Usuario/Correo/Clave Invalidas", "error")
        return redirect("/")

    session['usuario_nombre'] = usuario.nombre
    session['usuario_id'] = usuario.id
    session['usuario_apellido'] = usuario.apellido

    return redirect('/home')



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/home')