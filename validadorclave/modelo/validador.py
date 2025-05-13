from abc import ABC, abstractmethod
from validadorclave.modelo.errores import NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoCumpleLongitudMinimaError, NoTienePalabraSecretaError

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) < self._longitud_esperada:
            raise NoCumpleLongitudMinimaError(f"La clave debe tener más de {self._longitud_esperada} caracteres")

    def _contiene_mayuscula(self, clave):
        for c in clave:
            if c.isupper():
                return True
        raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")

    def _contiene_minuscula(self, clave):
        for c in clave:
            if c.islower():
                return True
        raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minuscula")

    def _contiene_numero(self, clave):
        for n in clave:
            if n.isdigit():
                return True
        raise NoTieneNumeroError("La clave debe contener al menos un número")

    @abstractmethod
    def es_valida(self, clave):
        pass

class ReglaValidacionGanimedes(ReglaValidacion):
    CARACTERES_ESPECIALES = {'@', '_', '#', '$', '%'}

    def __init__(self):
        super().__init__(8)

    def _contiene_caracter_especial(self, clave):
        for c in clave:
            if c in self.CARACTERES_ESPECIALES:
                return True
        raise NoTieneCaracterEspecialError("La clave debe contener al menos un carácter especial (@, _, #, $, %)")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self._contiene_caracter_especial(clave)
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def _contiene_calisto(self, clave):
        palabra = "calisto"
        clave_lower = clave.lower()
        if palabra not in clave_lower:
            raise NoTienePalabraSecretaError("La clave debe contener la palabra 'calisto'")

        conteo_mayusculas = sum(1 for c in clave if c.isupper())

        if conteo_mayusculas < 2 or conteo_mayusculas >= len(palabra):
            raise NoTienePalabraSecretaError("La palabra 'calisto' debe estar escrita con al menos dos letras en mayúscula, pero no todas")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_numero(clave)
        self._contiene_calisto(clave)
        return True

class Validador:
    def __init__(self, regla):
        self.regla = regla
    def es_valida(self, clave):
        return self.regla.es_valida(clave)



