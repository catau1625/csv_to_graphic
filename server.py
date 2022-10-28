from flask_crud.__init__ import app
from flask_crud.controllers import  usuarios,archivos
import os

if __name__ == "__main__":
    app.run(debug=True)