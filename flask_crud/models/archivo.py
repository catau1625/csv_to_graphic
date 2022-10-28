import os
from flask import flash
from flask_crud.config.mysqlconnection import connectToMySQL
from flask_crud.utils.regex import REGEX_CORREO_VALIDO


class File:
    def __init__(self,datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.data = datos['data']
        self.created_at = datos['created_at']
        self.usuario_id = datos['usuario_id']
        
    @classmethod
    def save_file(cls,data):
        query = "INSERT INTO archivos (nombre,data,created_at,usuario_id) VALUES (%(nombre)s,%(data)s,NOW(),%(usuario_id)s);"
        return connectToMySQL('esquema_excel').query_db(query,data)
    
    @classmethod
    def get_file_by_name(cls,data):
        query = "SELECT * FROM archivos WHERE nombre = %(nombre)s;"
        results = connectToMySQL('esquema_excel').query_db(query,data)
        file = []
        for info in results:
            file_data = {
                "id": info['id'],
                "nombre": info['nombre'],
                "data": info['data'],
                "created_at": info['created_at'],
                "usuario_id": info['usuario_id']
            }
            file.append(File(file_data))
        return file[0]
            
    