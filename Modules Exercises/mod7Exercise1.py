## Creación de un bucle 'While'

userInput = ''
planets = []

# Ciclo while para la entrada de planetas:

while userInput.lower() != 'done':
    userInput = input('Please insert a planet, start with upper case and write "done" when you done.\n') 
    planets.append(userInput) ## Add the last input from the user to the list of planets

planets.pop() # Delete 'done' from planets list

print(planets)