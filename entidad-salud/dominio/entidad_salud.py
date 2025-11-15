import json

from functions_json import read_json

class EntidadSalud:                       
    def __init__(self, nombre):
        self.nombre_entidad = nombre
        self.personal_medico = {}
        self.usuarios = {}
        self.citas_agendadas = {}
        self.servicios = [""]
        self.usuarios_json()

    def __len__(self):
        return len(self.personal_medico)
    
    def __str__(self):
        return f"""{self.nombre_entidad}"""

    def usuarios_json(self):
        usuarios_json = read_json()
        for usuario in usuarios_json:
            self.usuarios[usuario["ID"]] = usuario