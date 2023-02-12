from flask_crud.__init__ import ALLOWED_EXTENSIONS,app
from flask import send_from_directory

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/Users/cataubilla/Desktop/Escritorio_cataubilla/PROGRAMACION/coding_dojo/proyectos/csv_to_graphic/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)
        