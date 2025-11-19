# Librerias
import click
import json
import random

# Modulos de clases
import dominio.personas as per
import dominio.citas as citas
import dominio.entidad_salud as ent_sl
import dominio.excepciones as excp
from dominio.funciones import read_usuarios_json, read_citas_json, read_personal_medico_json, generador_codigo_cita


# Entidad de Salud (IPS)
ips = ent_sl.EntidadSalud("IPS__Prueba")


# Comandos
@click.group()
def cli():
    pass


@cli.command()
def usuarios():
    """Comando que permite visualizar todos los usuarios regsitrados en la Entidad de Salud"""
    for usuario in ips.usuarios.values():
        print(f"{usuario["ID"]} - {usuario["Nombre"]}")


@cli.command()
def nuevo_usuario():
    """Comando que permite registrar un nuevo usuario"""
    print("PARA CREAR EL USUARIO INGRESE LOS DATOS QUE A CONTINUACIÓN SE SOLICITAN")
    nombre, edad, sexo = input("NOMBRE: "), input("EDAD: "), input("SEXO - (F para femenino / M para masculino): ")
    id, email, numero_telefonico = input("ID: "), input("EMAIL: "), input("NÚMERO DE TELEFONO: ")
    regimen = input("TIPO DE RÉGIMEN - (Subsidiado / Contributivo): ")
    
    if id in ips.usuarios:
        raise excp.UsuarioInvalidoError("Usuario ya regsitrado")
    
    try:
        usuario = per.Usuario_IPS(nombre, int(edad), id, email, numero_telefonico, sexo, regimen)
        ips.usuarios[usuario.id] = usuario
        usuario_json = {"Nombre" : usuario.nombre,
                        "ID" : usuario.id,
                        "Edad" : usuario.edad,
                        "Sexo" : usuario.sexo,
                        "Número de telefono" : usuario.numero_telefonico,
                        "Email" : usuario.email,
                        "Regimen" : regimen}
        usuarios = read_usuarios_json()
        usuarios.append(usuario_json)
        with open("entidad-salud/datos/usuarios.json", "w", encoding = "utf8") as usuarios_json:
                json.dump(usuarios, usuarios_json, indent = 4)

    except excp.AfiliacionError as error:
        print(f"Error de afiliación de usuario: {error}")


@cli.command()
def eliminar_usuario():
    """Comando que permite la eliminación de un usuario"""
    id = input("Ingrese el ID del usuario: ")
    if id in ips.usuarios:
        del ips.usuarios[id]
        usuarios = read_usuarios_json()
        usuarios_actualizados = list(filter(lambda usuario: usuario["ID"] != id, usuarios))
        with open("entidad-salud/datos/usuarios.json", "w", encoding = "utf8") as usuarios_json:
            json.dump(usuarios_actualizados, usuarios_json, indent = 4)


@cli.command()
def agendar_cita():
    """Comando que permite agendar citas"""
    id_usuario = input("Ingrese el ID del usuario: ")
    if id_usuario in ips.usuarios:
        usuario = ips.usuarios[id_usuario]
        if not usuario.afiliado:
            raise excp.AfiliacionError("Problemas con la afiliación del usuario")
        while True:
            codigo_cita = generador_codigo_cita()
            if codigo_cita not in ips.citas_agendadas:
                break
        print("PARA AGENDAR LA CITA INGRESE LOS DATOS QUE A CONTINUACIÓN SE SOLICITAN")
        id_medico = input("Ingrese el ID del medico: ")
        especialidad = input("Ingrese la especialidad de la cita: ")
        if id_medico in ips.personal_medico:
            medico = ips.personal_medico[id_medico]
            if especialidad not in medico.especialidades:
                raise excp.MedicoInvalidoError(f"El medico no esta autorizado para realizar citas de {especialidad}")
            modalidad = input("Ingrese la modalidad de la cita (Presencial/Virtual): ")
            valor_cita = float(input("Ingrese el valor de la cita: "))
            fecha = input("Ingrese la fecha de la cita en formato (YYYY-MM-DD): ")
            hora_inicio_cita = input("Ingrese la hora de inicio de la cita en formato (HH:MM): ")
            hora_fin_cita = input("Ingrese la hora de fin de la cita en formato (HH:MM): ") 
            citas_agendadas = medico.citas_agendadas
            for inicio_cita, fin_cita in citas:
                condicion = (hora_fin_cita <= inicio_cita) or (hora_inicio_cita >= fin_cita)
                if not condicion:
                    raise excp.HorrarioAgendadoError("El medico ya tiene agendado ese horario")
            cita = citas.Cita(codigo_cita, usuario, fecha, hora_inicio_cita, hora_fin_cita,
                              especialidad, modalidad, medico, valor_cita)
            ips.citas_agendadas[cita.codigo_cita] = cita
            cita_json = {cita.codigo_cita, cita.usuario, cita.fecha, cita.hora_inicio, cita.hora_fin,
                         cita.especialidad, cita.modalidad, cita.medico, cita.valor_cita}
            citas_json = read_citas_json()
            citas_json.append(cita_json)
            with open("entidad-salud/datos/citas_json.json", "w", encoding = "utf8") as citass_json:
                    json.dump(citas_json, citass_json, indent = 4)
        else:
            raise excp.MedicoInvalidoError(f"Medico no registrado en {ips.nombre_entidad}")
    else:
        raise excp.UsuarioInvalidoError(f"Usuario no registrado en {ips.usuarios}")


if __name__ == '__main__':
    cli()






