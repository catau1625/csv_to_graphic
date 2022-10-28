import os
from flask import Flask
from flask_bcrypt import Bcrypt

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'clavesecreta'
