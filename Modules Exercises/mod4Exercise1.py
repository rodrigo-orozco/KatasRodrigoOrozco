# En este ejercicio, usarás métodos de cadena para modificar el texto con hechos sobre la Luna y 
# luego extraerás información para crear un breve resumen.

# Primero, divide el texto en cada oración para trabajar con su contenido:

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

parts = text.lower()
parts = text.split('.')


print(parts)

for item in parts:
    if (item.count('average') >= 1 | item.count('temperature') >= 1 | item.count('distance') >= 1):
        print(item)
    if (item.count('C') >= 1):
        item.replace('C', 'Celsius')

text = '.'.join(parts)

print(text)