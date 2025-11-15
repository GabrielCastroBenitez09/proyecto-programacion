class EntidadSalud:                       
    def __init__(self, nombre, servicios):    
        self.nombre_entidad = nombre_entidad
        self.personal_medico = {}  
        self.pacientes, self.citas_agendadas = {}, {}  
        self.servicios = servicios

    def __len__(self):
        return len(self.personal_medico)