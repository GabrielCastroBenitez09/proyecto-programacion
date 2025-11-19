import json
import random

def generador_codigo_cita():
    "Función que genera codigos aleatorios para las citas medicas"
    codigo = ""
    for _ in range(5):
        codigo += random.choice("0123456789")
    return codigo

#Funciones que leen los archivos '.json' de la entidad de salud (personal_salud.json, usuarios.jason, citas.json)
def read_usuarios_json():
    """Función qu"""
    with open("entidad-salud/datos/usuarios.json", "r", encoding = "utf8") as usuarios_json:
        usuarios = json.load(usuarios_json)
    return usuarios

def read_personal_medico_json():
    """Función qu"""
    with open("entidad-salud/datos/personal_medico.json", "r", encoding = "utf8") as personal_json:
        personal = json.load(personal_json)
    return personal

def read_citas_json():
    """Función qu"""
    with open("entidad-salud/datos/citas.json", "r", encoding = "utf8") as citas_json:
        personal = json.load(citas_json)
    return personal