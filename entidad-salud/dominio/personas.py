from dominio.excepciones import AfiliacionError
from dominio.regimen import Subsidiado, Contributivo

class Persona:
    """Clase base Persona"""
    def __init__(self, nombre, edad, sexo, id, email, numero_telefonico):
        self.nombre, self.edad, self.sexo = nombre, edad, sexo   #Edad debe ser validado, por cuestiones de no menor o igual a 0
        self.id, self.email, self.numero_telefonico = id, email, numero_telefonico  #sexo solo puede permitir 2 F o M

    def __repr__(self):
        return self.nombre

    def __str__(self):
        return f"""{self.nombre.upper()} - {self.id}"""
    
    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.id == other.id
            

class Usuario_IPS(Persona):
    """Clase Usuario que hereda de Persona.
        Inicializa los atributos de los usarios de la entidad de salud"""
    def __init__(self, nombre, edad, id, email, numero_telefonico, sexo, regimen):
        super().__init__(nombre, edad, sexo, id, email, numero_telefonico)
        self.afiliado = True
        self.citas_activas = {}
        self.historia_citas = {}
        
        if regimen == "Subsidiado":
            self.regimen = Subsidiado()
        elif regimen == "Contributivo":
            self.regimen = Contributivo()
        else:
            raise AfiliacionError("Tipo de regimen invalido")

    def __repr__(self):
        if self.afilidiado:
            return f"""Nombre: {self.nombre}, Afiliación: ACTIVA, Regimen: {self.regimen}"""
        return f"""Nombre: {self.nombre}, Afiliación: INACTIVA, Regimen: {self.regimen}"""
            
    def __str__(self):
        return f"""{self.nombre.upper()}

        DATOS PERSONALES
        -----------------
        ID: {self.id}
        Edad: {self.edad}
        Sexo: {self.sexo}

        DATOS DE CONTACTO
        -----------------
        Número Telefónico: {self.numero_telefonico}
        Email: {self.email}
        """

    def __len__(self):
        return len(self.citas)




class Medico(Persona):
    """Clase Medio que hereda de Persona.
        Reservado para el personal medico de la entidad de salud"""
    def __init__(self, nombre, edad, sexo, id, email, numero_telefonico, especialidades):
        super().__init__(self, nombre, edad, sexo, id, email, numero_telefonico)
        self.especialidades = especialidades
        self.citas_agendadas = {}
        
    def __repr__(self):
        return f"""Nombre: {self.nombre}"""
    
    def __str__(self):
        return f"""{self.nombre.upper()}
        Medico
        
        DATOS PERSONALES
        -----------------
        ID: {self.id}
        Edad: {self.edad}
        Sexo: {self.sexo}

        DATOS DE CONTACTO
        -----------------
        Número Telefónico: {self.numero_telefonico}
        Email: {self.email}
        """
