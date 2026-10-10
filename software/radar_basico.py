nombre = "Radar del Dragon"
esferas_detectadas = 7
distancia = 27.2
bateria = 100


print("===  Radar Dragon  ===")
print("Dispositivo: ", nombre)

if esferas_detectadas > 0:
    print("Dragon Balls detectadas:", esferas_detectadas)

    if distancia <= 15:
        print("¡Hay una Dragon Ball cerca!")
    else:
        print("Hay esferas, pero están lejos.")

else:
    print("No se detectaron Dragon Balls")



def comprobar_bateria(bateria):
    if bateria < 20:
        return "Advertencia: Bateria baja, recargar pronto."
    elif bateria < 60:
        return "Bateria en nivel medio, considerar recargar."
    else:
        return "Bateria en buen estado."
estado = comprobar_bateria(15)
print(estado)