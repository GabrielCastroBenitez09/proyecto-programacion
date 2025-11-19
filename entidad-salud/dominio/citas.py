# Excepciones
from dominio.excepciones import MedicoInvalidoError, UsuarioInvalidoError, AfiliacionError, TransaccionInvalidaError

class Cita:
    """Objeto Cita Medica"""
    def __init__(self, codigo_cita, usuario, fecha, hora_inicio, hora_fin, 
                 especialidad, modalidad, medico, valor_cita):  
        self.codigo_cita, self.fecha = codigo_cita, fecha, 
        self.hora_inicio, self.hora_fin = hora_inicio, hora_fin
        self.valor_cita, self.facturada = valor_cita, False
        self.especialidad, self.modalidad = especialidad, modalidad
        
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
        Fehca y Hora: {self.fecha} 
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

    def __facturar__(self, usuario, pago):
        if isinstance(usuario.regimen, Contributivo):
            if pago == self.valor_cita:
                self.facturada = True
                return f"""CITA FACTURADA
                
                Especialidad: {self.expecialidad}
                Código Cita: {self.codigo_cita}
                Fehca y Hora: {self.fecha} 
                Modalidad: {self.modalidad}
                Doctor Asignado: {self.medico.nombre}"""
            else:
                raise TransaccionInvalidaError("""PAGO RECHAZADO - MONTO INCORRECTO""")
            
        elif isinstance(usuario.regimen, Subsidiado):
            self.facturada = True
            return f"""CITA FACTURADA
            
            Especialidad: {self.expecialidad}
            Código Cita: {self.codigo_cita}
            Fehca y Hora: {self.fecha} 
            Modalidad: {self.modalidad}
            Doctor Asignado: {self.medico.nombre}"""
        else:
            raise AfiliacionError("Tipo de afiliación invalida")
