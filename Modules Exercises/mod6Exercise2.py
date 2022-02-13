## TRABAJANDO CON DATOS DE UNA LISTA

# Lista de planetas:

from fileinput import close


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Solicitar al usuario el nombre de un planeta:

userPlanet = input('Please, insert the name of the planet starting with Uppercase: ')

# Encontrar el planeta en la lista:

userPlanetIndex = planets.index(userPlanet)

# Mostrar planetas más cercanos al Sol que de el que el usuario registró:

closerPlanets = planets[0:userPlanetIndex]
print(f'The planets closer to the Sun than which you entered are: {closerPlanets}')

# Mostrar planetas más alejados al Sol que de el que el usuario registró:

fartherPlanets = planets[userPlanetIndex:]
print(f'{fartherPlanets} are planets farther to the Sun than which you entered.')