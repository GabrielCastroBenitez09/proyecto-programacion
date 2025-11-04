class EntidadSalud:                          #Añadir caracteristicas por tipo de entidad (Publica o Privada)
    def __init__(self, nombre, capital, servicios):     #como financiamiento del gobierno y cambios en el cobro a pacientes
        self.nombre, self._capital = nombre, capital
        self.personal_medico = {"Enfermeros":{}, "Medicos":{}, "Cirujanos":{}}  #Historial de los profesionales y reporte de desempeño
        self.pacientes, self.citas_agendadas = {}, {}     #Considerar agregar como atributo el catalogo de servicios
        self.servicios = servicios

    @property
    def capital(self):
        return self._capital

    @capital.setter
    def capital(self, valor):
        if valor <= 0:
            raise TransaccionInvalidaError("Cantidad invalida ingresada")
        self._capital = valor

    def __len__(self):
        return len(self.personal_medico)

    def contratar_personal(self, medico, sueldo):
        if medico.id not in self.personal_medico.values():
            self.personal_medico[medico.id] = medico
            self.personal_medico[medico.id].sueldo = sueldo
        else:
            raise MedicoInvalidoError("Medico ya contratado")

#Añadr razón de despido (justificado o injustificado).
#Por consiguiente validación para liquidar, caso que añade calculos adicionales dado el tiempo de permanencia entre otras cosas.
#Despido por razones de sanción, faltas, etc, puede incluir una marca en la hoja de vida y vetar al despedidio
    def despedir_personal(self, medico):
        del self.personal_medico[medico.id].sueldo
        del self.personal_medico[medico.id]

    def registrar_paciente(self, nombre, edad, id, email, numero_telefonico, sexo, genero):
        paciente = Paciente(nombre, edad, id, email, numero_telefonico, sexo, genero)
        self.pacientes[paciente.nombre] = paciente

    def pago_sueldos(self):
        for empleado in self.personal_medico.values():
            self.capital -= empleado.sueldo
