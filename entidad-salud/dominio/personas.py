class Persona:
    def __init__(self, nombre, edad, sexo, id, email, numero_telefonico):
        self.nombre, self.edad, self.sexo = nombre, edad, sexo
        self.id, self.email, self.numero_telefonico = id, email, numero_telefonico

    def __repr__(self):
        return self.nombre

    def __str__(self):
        return f"""{self.nombre.upper()} - {self.id}"""
    
    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.id == other.id
            

class Usuario_IPS(Persona):
    def __init__(self, nombre, edad, id, email, numero_telefonico, sexo, genero, regimen):
        super().__init__(nombre, edad, sexo, id, email, numero_telefonico)
        self.afiliado = True
        self.citas = {}
        
        if regimen != "Subsidiado" and regimen != "Contributivo":
            raise AfiliacionError("Tipo de regimen invalido")
        else:
            self.regimen = regimen

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
    def __init__(self, nombre, edad, sexo, id, email, numero_telefonico, especialidades):
        super().__init__(self, nombre, edad, sexo, id, email, numero_telefonico)
        self.especialidades = especialidades
        
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
