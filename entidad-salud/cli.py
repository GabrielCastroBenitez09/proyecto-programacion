# Librerias
import json
import random
import sys 

# Modulos de clases
import dominio.personas as per
import dominio.citas as citas
import dominio.entidad_salud as ent_sl
import dominio.excepciones as excp
from dominio.funciones import read_usuarios_json, read_citas_json, read_personal_medico_json, generador_codigo_cita
from dominio.regimen import Subsidiado, Contributivo # Necesario para la función facturar_cita

# Entidad de Salud (IPS)
ips = ent_sl.EntidadSalud("IPS__Prueba", servicios = ["Medicina General", "Pediatría", "Cardiología", 
                          "Terapia Física", "Nutrición", "Odontología"])


# Comandos
def usuarios():
    """Comando que permite visualizar todos los usuarios regsitrados en la Entidad de Salud"""
    try:
        for usuario in ips.usuarios.values():
            print(f"{usuario.id} - {usuario.nombre}")
    except Exception as e:
        print(f"Error en la visualización de usuarios. {e}")


def nuevo_usuario():
    """Comando que permite registrar un nuevo usuario y guardar sus datos en el JSON."""
    try:
        print("PARA LA CREACIÓN DEL USUARIO INGRESAR LOS SIGUIENTES DATOS")
        
        nombre = input("NOMBRE: ")
        edad = input("EDAD: ")
        sexo = input("SEXO - (F para femenino / M para masculino): ")
        id = input("ID: ")
        email = input("EMAIL: ")
        numero_telefonico = input("NÚMERO DE TELEFONO: ")
        regimen = input("TIPO DE RÉGIMEN - (Subsidiado / Contributivo): ")
        
        if id in ips.usuarios:
            raise excp.UsuarioInvalidoError("Usuario ya registrado")
        
        usuario = per.Usuario_IPS(nombre, int(edad), id, email, numero_telefonico, sexo, regimen)
        ips.usuarios[usuario.id] = usuario
        
        usuario_json = {
            "Nombre": usuario.nombre,
            "ID": usuario.id,
            "Edad": usuario.edad,
            "Sexo": usuario.sexo,
            "Número de telefono": usuario.numero_telefonico,
            "Email": usuario.email,
            "Regimen": regimen
        }
        
        usuarios = read_usuarios_json() 
        usuarios.append(usuario_json)
        
        with open("entidad-salud/datos/usuarios.json", "w", encoding="utf8") as usuarios_json_file:
            json.dump(usuarios, usuarios_json_file, indent=4)
        
        print(f"Usuario {nombre} registrado.")

    except excp.AfiliacionError as e:
        print(f"Error de afiliación de usuario: {e}")
    except excp.UsuarioInvalidoError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error. Valor ingresado para edad inválido")
    except Exception as e:
        print(f"ERROR. {e}")


def eliminar_usuario():
    try:
        id_usuario = input("Ingrese el ID del usuario: ")
        if id_usuario in ips.usuarios:
            del ips.usuarios[id_usuario] 

            usuarios = read_usuarios_json()
            usuarios_actualizados = list(filter(lambda usuario: usuario["ID"] != id_usuario, usuarios)) 
            
            with open("entidad-salud/datos/usuarios.json", "w", encoding = "utf8") as usuarios_json:
                json.dump(usuarios_actualizados, usuarios_json, indent = 4)

            print(f"Usuario {id_usuario} eliminado.")
        else:
             print(f"Usuario no encontrado.")
    except Exception as e:
        print(f"ERROR. {e}")


def agendar_cita():
    """Comando que permite agendar citas, crear el objeto Cita y guardar en JSON."""
    try:
        id_usuario = input("Ingrese el ID del usuario: ")
        if id_usuario not in ips.usuarios:
            raise excp.UsuarioInvalidoError(f"Usuario no registrado en {ips.nombre_entidad}")
        
        usuario = ips.usuarios[id_usuario]
        
        if not usuario.afiliado:
            raise excp.AfiliacionError("Problemas con la afiliación del usuario")
        
        while True:
            codigo_cita = generador_codigo_cita()
            if codigo_cita not in ips.citas_agendadas:
                break

        print("PARA AGENDAR LA CITA INGRESE LOS SIGUIENTES DATOS")
        
        id_medico = input("Ingrese el ID del medico: ")
        if id_medico not in ips.personal_medico:
            raise excp.MedicoInvalidoError(f"Médico no registrado en {ips.nombre_entidad}")
        
        medico = ips.personal_medico[id_medico] 
        
        especialidad = input("Ingrese la especialidad de la cita: ")
        if especialidad not in medico.especialidades:
            raise excp.MedicoInvalidoError(f"El médico no está autorizado para realizar citas de {especialidad}")
        
        modalidad = input("Ingrese la modalidad de la cita (Presencial/Virtual): ")
        valor_cita = float(input("Ingrese el valor de la cita: "))
        fecha = input("Ingrese la fecha de la cita en formato (YYYY-MM-DD): ")
        hora_inicio_cita = input("Ingrese la hora de inicio de la cita en formato (HH:MM): ")
        hora_fin_cita = input("Ingrese la hora de fin de la cita en formato (HH:MM): ") 
        
        citas_dia = medico.citas_agendadas.get(fecha, [])
        
        for inicio_existente, fin_existente in citas_dia:
            condicion = (hora_fin_cita <= inicio_existente) or (hora_inicio_cita >= fin_existente)
            if not condicion:
                raise excp.HorrarioAgendadoError("El médico ya tiene agendado ese horario")
        
        cita = citas.Cita(codigo_cita, usuario, fecha, hora_inicio_cita, hora_fin_cita,
                          especialidad, modalidad, medico, valor_cita)
        
        ips.citas_agendadas[cita.codigo_cita] = cita
        usuario.citas_activas[cita.codigo_cita] = cita
        
        medico.citas_agendadas.setdefault(fecha, []).append((hora_inicio_cita, hora_fin_cita))
        
        cita_json = {
            "Código Cita": cita.codigo_cita, 
            "Usuario": cita.usuario.id, 
            "Fecha": cita.fecha, 
            "Hora Inicio": cita.hora_inicio, 
            "Hora Fin": cita.hora_fin, 
            "Especialidad": cita.especialidad, 
            "Modalidad": cita.modalidad, 
            "Medico": cita.medico.id, 
            "Valor Cita": cita.valor_cita,
            "facturada": cita.facturada 
        }
        
        citas_json_list = read_citas_json()
        citas_json_list.append(cita_json)
        
        with open("entidad-salud/datos/citas.json", "w", encoding="utf8") as citass_json_file:
            json.dump(citas_json_list, citass_json_file, indent=4)
        
        print("Cita agendada.")
        
    except ValueError:
        print("ERROR. Valor de cita ingreasdo inválido. porfavor ingresar el valor númerico adecuado")
    except excp.UsuarioInvalidoError as e:
        print(f"ERROR. Problemas con la verificación del usuario. {e}")
    except excp.MedicoInvalidoError as e:
        print(f"ERROR. Problemas con el medico elegido. {e}")
    except excp.HorrarioAgendadoError as e:
        print(f"ERROR. Problemas con el horario elegido {e}")
    except Exception as e:
        print(f"ERROR. {e}")


def cancelar_cita():
    try:
        id_usuario = input("Ingrese su ID: ")
        if id_usuario not in ips.usuarios:
            raise excp.UsuarioInvalidoError(f"El usuario no está afiliado en {ips.nombre_entidad}") 
        
        usuario = ips.usuarios[id_usuario]
        codigo_cita = input("Ingrese el código de la cita que desea cancelar: ")
        usuario.cancelar_cita(codigo_cita) 
        del ips.citas_agendadas[codigo_cita] 
        
        citas_actuales = read_citas_json()
        citas_agendadas_json = list(filter(lambda cita: cita["Código Cita"] != codigo_cita, citas_actuales))
        
        with open("entidad-salud/datos/citas.json", "w", encoding = "utf8") as citas_json:
             json.dump(citas_agendadas_json, citas_json, indent = 4)
        
        print(f"Cita cancelada.")

    except excp.UsuarioInvalidoError as e:
        print(f"ERROR. Problemas con la verificación del usuario. {e}")
    except Exception as e:
        print(f"ERROR.")


def informacion_usuario():
    try:
        id_usuario = input("Ingrese del ID del usuario: ")
        if id_usuario not in ips.usuarios:

            raise excp.UsuarioInvalidoError(f"El usuario no está afiliado en {ips.nombre_entidad}")
        else:

            usuario = ips.usuarios[id_usuario]
            print(usuario)

    except excp.UsuarioInvalidoError as e:
        print(f"ERROR. Usuario no existente. {e}")


def consulta_citas_usuario():
    try:
        id_usuario = input("Ingrese su ID: ")
        if id_usuario not in ips.usuarios:
            raise excp.UsuarioInvalidoError(f"El usuario no está afiliado en {ips.nombre_entidad}")
        usuario = ips.usuarios[id_usuario]

        print(f"El usuario tiene {len(usuario)} citas activas")

        if len(usuario) == 0:
            return
        
        for cita in usuario.citas_activas.values():
            print("----------------------------------")
            print(cita)

    except excp.UsuarioInvalidoError as e:
        print(f"ERROR. Usuario no existente. {e}")


def facturar_cita():
    try:
        codigo_cita = input("Ingrese el código de la cita: ")
        if codigo_cita not in ips.citas_agendadas:
            raise excp.TransaccionInvalidaError(f"Cita con código '{codigo_cita}' no registrada")
            
        id_usuario = input("Ingrese el ID del usuario: ")
        if id_usuario not in ips.usuarios:
            raise excp.UsuarioInvalidoError("El usuario no está afiliado")
            
        usuario = ips.usuarios[id_usuario]
        cita = ips.citas_agendadas[codigo_cita]

        if isinstance(usuario.regimen, Subsidiado):
            pago = 0.0
        elif isinstance(usuario.regimen, Contributivo):
            valor_requerido = cita.valor_cita 
            print(f"Valor Cita: ${valor_requerido:,.2f}")
            pago = float(input("Ingrese el pago (Valor exacto): "))
        else:
            pago = float(input("Ingrese el pago: ")) 
            
        cita.facturar(usuario, pago)
     
        citas_existentes = read_citas_json()
        for i, cita_dict in enumerate(citas_existentes):
            if cita_dict.get("Código Cita") == codigo_cita:
                citas_existentes[i]["facturada"] = True 
                citas_existentes[i]["estado"] = "Facturada" 
                break
        
        with open("entidad-salud/datos/citas.json", "w", encoding="utf8") as citas_json_file:
            json.dump(citas_existentes, citas_json_file, indent=4)
        
        print("Cita facturada.")

    except excp.TransaccionInvalidaError as e:
        print(f"ERROR. Problemas con la transacción: {e}")
    except excp.UsuarioInvalidoError as e:
        print(f"ERROR. Problemas con la verificación del usuario: {e}")
    except ValueError:
        print("ERROR. Tipo de pago incorrecto.")
    except Exception as e:
        print(f"ERROR: {e}")


# Linea de Comando
def main():
    print(f"-----------------------------------------------------")
    print(f"         Sistema de Gestión {ips.nombre_entidad}     ")
    print(f"-----------------------------------------------------")

    # Lista de comando
    comandos = {
        "1": usuarios,
        "2": nuevo_usuario,
        "3": eliminar_usuario,
        "4": agendar_cita,
        "5": cancelar_cita,
        "6": informacion_usuario,
        "7": consulta_citas_usuario,
        "8": facturar_cita
    }

    while True:
        print("MENÚ DE OPERACIONES")
        print("---------------------------")
        print("1. Visualizar Usuarios")
        print("2. Registrar Nuevo Usuario")
        print("3. Eliminar Usuario")
        print("4. Agendar Cita")
        print("5. Cancelar Cita")
        print("6. Ver Información de Usuario")
        print("7. Consultar Citas Activas del Usuario")
        print("8. Facturar Cita")
        print("0. SALIR")
        print("---------------------------")
        
        opcion = input("Ingrese el número del comando: ").strip()

        if opcion == '0' or opcion.lower() == 'salir':
            print("CIERRE DE SISTEMA.")
            sys.exit(0)
        
        if opcion in comandos:
            comandos[opcion]() 
        else:
            print(f"ERROR. {opcion} no existe.")


if __name__ == '__main__':
    main()