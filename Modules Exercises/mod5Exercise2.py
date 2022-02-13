## E2.- Converitir cadenas en números y usar valores absolutos

## Tomando los valores del usuario

planet1 = int(input("Ingrese la distancia al sol del primer planeta: "))
planet2 = int(input("Ingrese la distancia al sol del segundo planeta: "))

## Caclculando distancia entre planetas

distPlanets = abs(planet1 - planet2)
print(f'Distancia entre los planetas en km: {distPlanets} km')

## Convirtiendo km a millass

distPlanetsMillas = distPlanets * 0.621
print(f'Distancia entre los planetas en mi: {distPlanetsMillas} mi')