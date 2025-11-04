class Persona:
    def __init__(self, nombre, edad, id, email, numero_telefonico):
        self.nombre , self.id, self.email, self.numero_telefonico, self.edad = nombre, id, email, numero_telefonico, edad

    def __str__(self):
        return {self.nombre}

    def __repr__(self):
        return f"""
        Nombre: {self.nombre}
        Edad: {self.edad}
        Email: {self.email}
        """
    #Podria el __len__ ser por la edad, pero realmente no creo que sea relevante


class Paciente(Persona):
    def __init__(self, nombre, edad, id, email, numero_telefonico, sexo, genero):
        super().__init__(nombre, edad, id, email, numero_telefonico)
        self.sexo, self.genero = sexo, genero
        self.citas = {}

    def __repr__(self):
        return f"""PACIENTE
        Nombre: {self.nombre}
        Edad: {self.edad}
        Genero: {self.genero}
        Numero Telefonico: {self.numero_telefonico}
        """

    def __len__(self):
        return len(self.citas)

    


#Posibilidad de añadir hoja de vida, con el historial de trabajos y posibles marcas en la hoja de vida (sanciones, despidos por faltas, etc)
#Sección de recomendaciones y referencias.  Añadir a la entidad de salud una valoración del profesional, para referir la referencia
class Personal(Persona):
    def __init__(self, nombre, edad, id, email, numero_telefonico, cargo):
        super().__init__(nombre, edad, id, email, numero_telefonico)
        self.cargo = cargo
    def __repr__(self):
        return f"""{self.cargo.upper()}
        Nombre: {self.nombre}
        Edad: {self.edad}
        Numero Telefonico: {self.numero_telefonico}
        Email: {self.email}
        """


class Enfermero(Personal):
    def __init__(self, nombre, edad, id, email, numero_telefonico):
        super().__init__(nombre, edad, id, email, numero_telefonico, cargo = "Enfermero/a")

    def __repr__(self):
        return super().__repr__()


class Medico(Personal):
    def __init__(self, nombre, edad, id, email, numero_telefonico, especialidades):
        super().__init__(nombre, edad, id, email, numero_telefonico, cargo = "Medico")
        self.especialidades = especialidades
        self.agenda = {}

    def __len__(self):
        return len(self.agenda)

    def __repr__(self):
        return super().__repr__() + f"""
        Especialidades: {self.especialidades}"""


class Cirujano(Medico):
    def __init__(self, nombre, edad, id, email, numero_telefonico, especialidades):
        super().__init__(nombre, edad, id, email, numero_telefonico, especialidades)
        self.cargo = "Cirujano"

    def __repr__(self):
        return super().__repr__()

