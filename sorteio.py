import random

listaTemas = ['1', '2', '3', '4', '5', '6']
listaGrupo = ['G1','G2','G3','G4','G5','G6']
tema = ''
grupo = ''
while (listaTemas != []):
    tema = random.choice(listaTemas)
    grupo = random.choice(listaGrupo)
    listaTemas.remove(tema)
    listaGrupo.remove(grupo)
    print(" O grupo ", grupo, "foi sorteado com o tema ", tema)
