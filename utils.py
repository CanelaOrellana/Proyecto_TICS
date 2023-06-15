# Imports
from datetime import datetime,time

# Umbral de temperatura
def temp_thresh(temp):
    now = datetime.now()
    # Determinar si el tiempo del PC es de noche o de día
    current_time = now.time()
    moment = "noche"
    msg = " "
    # Noche
    if current_time >= time(23,00) or current_time <= time(7,00):
        # Límites: link de referencia http://www.abcagro.com/hortalizas/poroto.asp
        if temp >= 16 and temp <= 18:
            msg = "Es de {} y hay {} grados, la temperatura de tu poroto es óptima para el crecimiento :)".format(moment,temp)
        elif temp < 16:
            msg = "Es de {} y hay {} grados, por favor abriga a tu poroto :(".format(moment,temp)
        elif temp > 18:
            msg = "Es de {}, por favor riega a tu poroto :(".format(moment)
    # Día
    else:
        moment = "día"
        if temp >= 21 and temp <= 28:
            msg = "Es de {} y hay {} grados, la temperatura de tu poroto es óptima para el crecimiento :)".format(moment,temp)
        elif temp < 21:
            msg = "Es de {} y hay {} grados, por favor abriga a tu poroto :(".format(moment,temp)
        elif temp > 28:
            msg = "Es de {}, por favor riega a tu poroto :(".format(moment)

    return msg

# Umbral de humedad
def hum_thresh(hum):
    msg = " "
    # Humedad óptima
    if hum >= 60 and hum <= 65:
        msg = "La humedad es de {}, óptima para tu poroto :)".format(hum)
    # Casos contrarios
    elif hum < 60:
        msg = "La humedad es de {}, por favor riega a tu poroto :(".format(hum)
    elif hum > 65:
        msg = "La humedad es de {}, no lo riegues más :(".format(hum)
    return msg
        