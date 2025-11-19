# Excepciones personalizadas

class UsuarioInvalidoError(Exception):
    """Excepción para problemas con los usuariso"""
    pass

class AfiliacionError(Exception):
    """Excepción para problemas con la afiliación del usuario"""
    pass
class MedicoInvalidoError(Exception):
    """Excepciónpara problemas con el personal medico"""
    pass

class HorrarioAgendadoError(Exception):
    """Excepción para problemas con los horarios de citas medicas"""
    pass

class TransaccionInvalidaError(Exception):
    """Execpción para problemas con pagos"""
    pass