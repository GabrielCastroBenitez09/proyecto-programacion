# 📌 Proyecto Programación II

Proyecto de Sistema de Gestión para Entidad de Salud (IPS).

Miembros: Grabiel Hernan Castro Benitez.

---

## Descripción

Proyecto enfocado en sistema de gestión de los usuarios de una entidad de salud. Aborda el regsitro de nuevos usuarios, la cancelación de la afiliación de los usuarios, el manejo y portal de consulta de los datos del usuario y su registro de citas medicas. Además controla la agenda de citas medicas y la facturación por parte de usuarios con los tipos de regimen soportados.

---

## 🚀 Funcionamiento

Entidad de salud inicializada con una pequeña base de personal medico y un listado de servicios.

El sistema permite:

- Crear nuevos usuarios: Usuarios afiliados a la entidad de salud, registrando datos peronales (nombre, edad, sexo, id), datos de contacto (email, número de telefono)

- Ver la lista de usuarios: Visualización de la lista completa de usuarios reistrados en la entidad de salud.

- Agendar citas: Valido unicamente para usuarios afiliados a la entidad de salud, agenda citas en una fecha y una hora (dada en la duración de la cita) con los profesionales de salud de la entidad que cuenten con las credenciales necesarias. Se ofrecen citas con modalida presencial y virtual.

- Cancelar citas: Cancelación de citas medicas por parte de los usuarios, elimina la cita de la base de datos, del listado de citas activas del usuarios y del horario del medico asignado.

- Eliminar usuarios: Elimina el registro y la afiliación de los usuarios a la entidad de salud.

- Ver la información del usuario: Lugar de consulta de datos del usuario.

- Consultar citas activas: Permite a los usuarios consultar el listado de citas medicas activas, además de proporcionar el estado de facturación de la cita.

- Facturación de citas: Recibe los pagos de citas medicas. Evalua cuestiones del regimen del paciente, gratis para usuarios de subsidiados, con coste y confirmación de pago para usuarios con regimen contributivos.

- Cerrar el sistema: Salida del sistema, detiene operaciones y comandos.

---


### 📋 Prerrequisitos

- Sistema Operativo (por ejemplo, Ubuntu 20.04, Windows 10)
- Lenguaje de programación: Python 3.10+

### 🔧 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/proyecto-programacion.git
cd proyecto-programacion

# Crear entorno virtual (opcional)
python -m venv venv
.\.venv\Scripts\activate 

# Ejecutar la aplicación
python .\entidad-salud\cli.py
```

Una vez ejecutada la aplicación, se despliega un menu de comandos, que se compone de los metodos y funcionalidades previamente descritas. Al marcar una de las opciones, se solicitaran datos especificos (información de usuarios, personal de la salud, horarios requeridos para las citas medicas, pagos, etc) para realizar las operaciones.

---

## 🛠️ Construido Con

- [Python](https://www.python.org/) - Lenguaje de programación

---
