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

    @abstractmethod
    def es_valida(self, clave):
        pass
