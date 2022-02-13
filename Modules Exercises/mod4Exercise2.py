from optparse import TitledHelpFormatter


name = 'Marte'
gravity = 0.00143 ## in kms
planet = 'Ganimedes'

title = f'Gravity facts about {name}'

title = title.title()

text = f"""Planet name: {planet}
Gravity on {name}: {gravity*1000}"""

print(title)
print('----------------------------------')
print(text)
