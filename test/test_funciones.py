# Via facil de llamar un modulo en otro lugar del directorio

#import sys,os
#sys.path.insert(0, os.path.abspath('...'))

import paquete.funciones as fun
fun.Luisa()
print(fun.veronica(2,10))

def test_prueba():
    assert fun.veronica(2,10) == 9

def test_suma():
    """
    Docuemntación suma
    """
    assert fun.sumar(5,4) == 9








