# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, 
# a veces produce un rayo de luz que se puede ver desde la Tierra. Escribe la lógica condicional que usa declaraciones
#  if, else, y elif para alertar a las personas de todo el mundo que deben buscar un asteroide en el cielo.
# ¡Hay uno que se dirige a la tierra ahora a una velocidad de 19 km/s!

asteroidVel = 19 #km/s

if asteroidVel >= 20:
    print("Mira hacia arriba! Enocontrarás el asteroide que impacatará en la Tierra!")
else:
    print("No hay peligro, continúe con su día")