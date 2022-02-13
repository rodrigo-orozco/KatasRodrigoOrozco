## USAR LISTAS PARA ALMACENAR NOMBRES DE PLANETAS

## Creando la lista de planetas

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Urano', 'Neptune']
print(f'There are {len(planets)} planets in the solar system.')
print(f'Those planets are: {planets}')

## Agregando a Plutón

planets.append('Pluto')
print(f'Actually, there are {len(planets)} in the solar system. This is because we added {planets[-1]}.')