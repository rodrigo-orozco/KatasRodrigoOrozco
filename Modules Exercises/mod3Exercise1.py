# Para este ejercicio, escribirás una lógica condicional que imprima una advertencia si un asteroide se acerca a la Tierra demasiado rápido.
# La velocidad del asteroide varía dependiendo de lo cerca que esté del sol, y cualquier velocidad superior a 25 kilómetros por segundo (km/s)
#  merece una advertencia.

# Un asteroide se acerca, y viaja a una velocidad de 49 km/s.

asteroidVel = 49 # km/s

if asteroidVel > 25:
    print("Peligro! el asteroide se acerca rápidamente")
else:
    print("No hay peligro, continúe con su día")