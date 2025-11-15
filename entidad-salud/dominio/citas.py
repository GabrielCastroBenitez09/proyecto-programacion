class Cita:
    def __init__(self, codigo_cita, usuario, hora, fecha, especialidad, modalidad, medico):   #Añair el valor de las citas
        self.codigo_cita = codigo_cita
        self.facturada = False
        
        if not usuario.afiliado:
            raise UsuarioInvalidoError("_______")
            
        if especialidad not in medico.especialidades:
            raise MedicoInvalidoError("_______")
        
    def __str__(self):
        return f"""CITA DE {self.especialidad.upper()}
        -----------------
        Código Cita: {self.codigo_cita}
        Fehca y Hora: {self.hora_fecha}
        Especialidad: {self.expecialidad}
        Modalidad: {self.modalidad}
        
        DATOS PACIENTE
        -----------------
        Nombre: {usuario.nombre}
        ID: {usuario.id}
        Edad: {usuario.edad}
        Sexo: {usuario.sexo}
        Numero Telefonico: {usuario.numero_telefonico}
        Email: {usuario.email}
        
        DATOS PROFESIONAL SALUD
        -----------------
        Nombre: {medico.nombre}
        ID: {medico.id}
        Numero Telefonico: {medico.numero_telefonico}
        Email: {medico.email}
        """

    def __repr__(self):
        return f"Cita {self.modalidad} de {self.especialidad} agendada para {self.hora}. {self.paciente.nombre}"
