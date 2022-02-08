asteroidVel = 23 # km/s
asteroidSize = 26 # m 

if (asteroidSize > 25 & asteroidSize < 1000) | (asteroidVel > 25):
    print("Cuidado! Un asteroide muy peligroso se acerca a la Tierra!")
elif asteroidSize >= 20:
    print("Look Up! Un asteroide se acerca a la Tierra")
elif asteroidVel < 25:
    print("No hay peligro inminente, continue con su dia :D")
else:
    print("No hay peligro inminente, contiue con su dia :D")