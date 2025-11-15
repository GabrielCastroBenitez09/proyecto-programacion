from dominio.excepciones import MedicoInvalidoError, UsuarioInvalidoError, AfiliacionError

class Cita:
    def __init__(self, codigo_cita, usuario, hora, fecha, especialidad, modalidad, medico):   #Añair el valor de las citas
        self.codigo_cita = codigo_cita
        self.facturada = False
        
        if not usuario.afiliado:
            raise UsuarioInvalidoError("_______")
        else:
            self.usuario = usuario

        if especialidad not in medico.especialidades:
            raise MedicoInvalidoError("_______")
        else:
            self.medico = medico

    def __str__(self):
        return f"""CITA DE {self.especialidad.upper()}
        -----------------
        Código Cita: {self.codigo_cita}
        Fehca y Hora: {self.hora_fecha}
        Especialidad: {self.expecialidad}
        Modalidad: {self.modalidad}
        
        DATOS PACIENTE
        -----------------
        Nombre: {self.usuario.nombre}
        ID: {self.usuario.id}
        Edad: {self.usuario.edad}
        Sexo: {self.usuario.sexo}
        Numero Telefonico: {self.usuario.numero_telefonico}
        Email: {self.usuario.email}
        
        DATOS PROFESIONAL SALUD
        -----------------
        Nombre: {self.medico.nombre}
        ID: {self.medico.id}
        Numero Telefonico: {self.medico.numero_telefonico}
        Email: {self.medico.email}
        """

    def __repr__(self):
        return f"Cita {self.modalidad} de {self.especialidad} agendada para {self.hora}. {self.paciente.nombre}"
