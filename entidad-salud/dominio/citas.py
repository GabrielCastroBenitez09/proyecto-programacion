class Cita:
    def __init__(self, entidad_salud, paciente, hora, fecha, especialidad, modalidad, medico):   #Añair el valor de las citas y cirugias
        if especialidad not in entidad_salud.servicios:
            raise AlgoError(f"{entidad_salud.__name__} no ofrece este servicio")
        if not isinstance(medico (Medico, Cirujano)):                                 #Considerar añadir cuestiones de financiamiento
            raise MedicoInvalidoError("El Medico elegido no esta habilitado para realizar citas medicas")
        else:
            self.paciente, self.especialidad, self.medico, = paciente, especialidad, medico
            self.hora, self.fecha, self.modalidad = hora, fecha, modalidad
            for servicio in entidad_salud.servicios:
                self.precio = servicio["Precio"]

    def __repr__(self):
        return f"""CITA DE {self.especialidad.upper()}
        Paciente: {self.paciente}
        Edad: {self.edad}
        Fehca y Hora: {self.hora_fecha}
        Modalidad: {self.modalidad}
        Medico Asignado: {self.medico.nombre}"""

    def __str__(self):
        return f"Cita {self.modalidad} de {self.especialidad} agendada para {self.hora}. {self.paciente.nombre}"


class Cirugia(Cita):
    def __init__(self, paciente, hora, fecha, especialidad, cirujano):
        if isinstance(cirujano, Cirujano):
            super().__init__(paciente, hora, fecha, especialidad, modalidad = "Presencial", medico = cirujano)
        else:
            raise MedicoInvalidoError("El Medico elegido no hace parte del personal hailitado para realizar cirugias")

    def __repr__(self):
        return f"""CIRUGIA DE {self.especialidad.upper()}
        Paciente: {self.paciente}
        Edad: {self.edad}
        Fehca y Hora: {self.hora_fecha}
        Cirujano Asignado: {self.cirujano.nombre}"""
