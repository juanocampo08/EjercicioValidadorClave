from validadorclave.modelo.validador import Validador

def validar_clave(clave, reglas):
    for regla in reglas:
        try:
            validador = Validador(regla)
            if validador.es_valida(clave):
                print(f" La clave es válida para {regla.__class__.__name__}")
        except ValueError as e:
            print(f" Error: {regla.__class__.__name__}: {e}")
