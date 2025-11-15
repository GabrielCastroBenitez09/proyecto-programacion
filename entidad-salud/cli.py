# Librerias
import click
import json
import os

# Modulos de clases
import dominio.personas as per
import dominio.citas as citas
import dominio.entidad_salud as ent_sl
import dominio.excepciones as excp
from functions_json import read_json

ips = ent_sl.EntidadSalud("IPS__Prueba")

@click.group()
def cli():
    pass

@cli.command()
def usuarios():
    for usuario in ips.usuarios.values():
        print(f"{usuario["ID"]} - {usuario["Nombre"]}")


@cli.command()
def nuevo_usuario():
    print("PARA CREAR EL USUARIO INGRESE LOS DATOS QUE A CONTINUACIÓN SE SOLICITAN")
    nombre, edad, sexo = input("NOMBRE: "), input("EDAD: "), input("SEXO - (F para femenino / M para masculino): ")
    id, email, numero_telefonico = input("ID: "), input("EMAIL: "), input("NÚMERO DE TELEFONO: ")
    regimen = input("TIPO DE RÉGIMEN - (Subsidiado / Contributivo): ")

    usuario = per.Usuario_IPS(nombre, edad, id, email, numero_telefonico, sexo, regimen)
    ips.usuarios[usuario.id] = {"Nombre" : usuario.nombre,
                                "ID" : usuario.id,
                                "Edad" : usuario.edad,
                                "Sexo" : usuario.sexo,
                                "Número de telefono" : usuario.numero_telefonico,
                                "Email" : usuario.email}
    usuarios = read_json()
    usuarios.append(ips.usuarios[usuario.id])
    with open("entidad-salud/datos/usuarios.json", "w", encoding = "utf8") as usuarios_json:
            json.dump(usuarios, usuarios_json, indent = 4)


@cli.command()
def eliminar_usuario():
    id = input("Ingrese el ID del usuario: ")
    if id in ips.usuarios:
        del ips.usuarios[id]
        usuarios = read_json()
        usuarios_actualizados = list(filter(lambda usuario: usuario["ID"] != id, usuarios))
        with open("entidad-salud/datos/usuarios.json", "w", encoding = "utf8") as usuarios_json:
            json.dump(usuarios_actualizados, usuarios_json, indent = 4)




if __name__ == '__main__':
    cli()






