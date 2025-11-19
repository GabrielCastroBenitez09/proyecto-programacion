import json
import dominio.personas as per
from dominio.excepciones import AfiliacionError 
from dominio.funciones import read_usuarios_json, read_citas_json, read_personal_medico_json

class EntidadSalud:                         
    def __init__(self, nombre):
        self.nombre_entidad = nombre
        self.personal_medico = {}
        self.usuarios = {}
        self.citas_agendadas = {}
        self.servicios = [""]

        self.usuarios_json()
        self.personal_medico_json()

    def __len__(self):
        return len(self.personal_medico)
    
    def __str__(self):
        return f"""{self.nombre_entidad}"""

    def usuarios_json(self):
        usuarios_json = read_usuarios_json()
        for usuario_json in usuarios_json:
            try:
                usuario = per.Usuario_IPS(
                    usuario_json["Nombre"], usuario_json["Edad"], usuario_json["ID"],
                    usuario_json["Email"], usuario_json["Número de telefono"], 
                    usuario_json["Sexo"], usuario_json["Regimen"])
            except AfiliacionError as error:
                print(f"Error de afiliación de usuario: {error}")

    def personal_medico_json(self):
        personal_medico_json = read_personal_medico_json()
        for medico in personal_medico_json:
            self.personal_medico[medico["ID"]] = medico