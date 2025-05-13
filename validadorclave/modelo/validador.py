from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise ValueError(f"La clave debe tener más de {self._longitud_esperada} caracteres")

    def _contiene_mayuscula(self, clave):
        tiene_mayuscula = False
        for c in clave:
            if c.isupper():
                tiene_mayuscula = True
                break
        if not tiene_mayuscula:
            raise ValueError("La clave debe contener al menos una letra mayúscula")

    def _contiene_minuscula(self, clave):
        tiene_minuscula = False
        for c in clave:
            if c.islower():
                tiene_minuscula = True
                break
        if not tiene_minuscula:
            raise ValueError("La clave debe contener al menos una letra minuscula")
    def _contiene_numero(self, clave):
        tiene_numero = False
        for n in clave:
            if n.isdigit():
                tiene_numero = True
                break
        if not tiene_numero:
            raise ValueError("La clave debe contener al menos un número")

    @abstractmethod
    def es_valida(self, clave):
        pass

class ReglaValidacionGanimedes(ReglaValidacion):
    CARACTERES_ESPECIALES = {'@', '_', '#', '$', '%'}

    def __init__(self):
        super().__init__(8)

    def _contiene_caracter_especial(self, clave):
        contiene_caracter_especial = False
        for c in clave:
            if c in self.CARACTERES_ESPECIALES:
                contiene_caracter_especial = True
                break
        if not contiene_caracter_especial:
            raise ValueError("La clave debe contener al menos un carácter especial (@, _, #, $, %)")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self._contiene_caracter_especial(clave)
        return True