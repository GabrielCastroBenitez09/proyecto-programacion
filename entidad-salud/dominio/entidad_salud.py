import json
from dominio.personas import Medico, Usuario_IPS
from dominio.excepciones import AfiliacionError 
from dominio.funciones import read_usuarios_json, read_citas_json, read_personal_medico_json

class EntidadSalud:                         
    def __init__(self, nombre, servicios):
        self.nombre_entidad = nombre
        self.personal_medico = {}
        self.usuarios = {}
        self.citas_agendadas = {}
        self.servicios = servicios

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
                usuario = Usuario_IPS(
                    usuario_json["Nombre"], usuario_json["Edad"], usuario_json["ID"],
                    usuario_json["Email"], usuario_json["Número de telefono"], 
                    usuario_json["Sexo"], usuario_json["Regimen"])
            except AfiliacionError as error:
                print(f"Error de afiliación de usuario: {error}")

    def personal_medico_json(self):
        personal_medico_json_list = read_personal_medico_json()
        
        for medico_dict in personal_medico_json_list:
            medico_obj = Medico(
                medico_dict["Nombre"],
                medico_dict["Edad"],
                medico_dict["Sexo"],
                medico_dict["ID"],
                medico_dict["Email"],
                medico_dict["Número de telefono"],
                medico_dict["Especialidades"] 
            )
            self.personal_medico[medico_obj.id] = medico_obj
            
            print(f"Médico {medico_obj.nombre} registrado.")

    def __iter__(self):
        """Itera sobre el personal medico de la entidad de salud."""
        for medico in self.personal_medico.values():
            yield medico