# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 16:38:48 2021

@author: @AZIZI  Sajajd
"""

import turtle
# Importer le module "turtle" dans le programme

######################################################################################
# COMMENT ÇA SE DÉROULE CE PROGRAMME :
# def sudokucarre():
    # Dessiner le carré principal
# def sudokucarreSmall():
    # Désinner les 9 carrés principaux , divisant le carré parincipal à 9 carré 
# def box(len):
    # La boucle "for" désinne les plus petits carrés 
    # Faire appel aux autres def 
# def lignesDictDef():
    # Permettant de couper la liste [carresid] à 9 ligne horizontales
# La boucle "While" (Ligne 151):
    # Configurer la vitesse + le police et la position initiale de la tortue +
    # lever er descendre le stylo et dépalcer la tortue si besoin
######################################################################################
# RESTE Â FAIRE : 
    # Finir le "def lignesDictDef()
    # Finir le "def colonnesDictDef()
    # Créer des modules pour remplir la grille sudoku "RESOLVER"
    

######################################################################################




#turtle.tracer(0)
# Ne pas afficher les mouvements de la tortue -> afficher directement le résultat final
# wn = turtle.Screen()
#wn.tracer(0)
## Deuxième méthode pour afficher le résultat final 



x = 0
y = 0

carresid = []
# Liste des petits carrés du premier au dernier [1 - 81]
# Dans la def--> def (box), après avoir dessién chaqu ecarré def ajoute un membre à la liste 
carreid = 0
# Utilisée dans le DEF BOX(LEN):
    # compteur des petits carré (les plus petits)
    # Dans la foncrion box(len :)
    # à chaque carré dessiné elle incrémente d'une unité (carreid += carreid)

colonnesDict = {}
# Dictionnaires des lignes horizentaales de [1 - 9]


lignesDict = {"ligne1":[],
            "ligne2":[],
            "ligne3":[],
            "ligne4":[],
            "ligne5":[],
            "ligne6":[],
            "ligne7":[],
            "ligne8":[],
            "ligne9":[]}


# Dictionnaires des colonnes Verticales de [1 - 9]



def sudokucarre():
    turtle.speed(0)
    turtle.goto(0,0)
    for i in range(1, 5):
        turtle.pensize(5)
        turtle.forward(450)
        print('i' ':', i)
        turtle.left(90)
        print('X:', int(turtle.xcor()), 'Y:', int(turtle.ycor()), ')',)


def sudokucarreSmall():
    turtle.speed(0)
    y = 0
    turtle.pensize(5)
    while y >= 0 and y < 300:
        y = y + 150       
        turtle.penup()
        turtle.goto(0, y)
        turtle.pendown()
        turtle.forward(450)
    x = 0
    turtle.left(90)
    while x >= 0 and x < 300:
       x = x + 150       
       turtle.penup()
       turtle.goto(x, 0)
       turtle.pendown()
       turtle.forward(450)
    return turtle.penup()

def box(len):
    # Utilisé dans la boucle WHILE, 
    # Variable (len) est la langueur des faces des patits carrés 
    print('*' * 20)
    global carreid
    global lignesDict
    # Définir les Variables "carreid" et "lignesDict" comme globales / 
    # car elle sont définies au niveau GLOBAL (La colonne VERTCALES PRICIPALE)
    carreid = carreid + 1
    # Incrémenter les carré ID 
    carresid.append(carreid)
    # Ajouter les "carreid" incrémentre (de la ligne précédente) à la liste [carresid]
    print(carresid)
    # Imprimer la liste [carresid]
    lignesDictDef()
    # Appeler la DEF "lignesDictDef", permettant de couper la liste [carresid] à 9 ligne horizontales
    print(lignesDictDef)
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)
        


def lignesDictDef():
    # lignesDictDef => permettant de couper la liste [carresid] à 9 ligne horizontales
    # for LineNuméro in range (9):
    global lignesDict
    if carreid <= 9:
        lignesDict['ligne1'].append(carreid)
    elif carreid <= 10 and carreid <= 18:
        lignesDict['ligne2'].append(carreid)
    print('%£%£µ' * 10, 'lignesDictDef')
    print(lignesDict)

'''

horizoncarres   [1 - 9]
verticauxcarres [1 - 9]
3x3carres [1 - 9]

carreid [1 - 81]
'''



'''
turtle.penup()
turtle.setx(-250)
turtle.sety(500)
turtle.pendown()
turtle.color('black')
style = ('Courier', 30, 'italic')

#turtle.write('CAMP Python 1400 _ Mohandes Shokri', font=style, align='center')
'''


sudokucarre()
sudokucarreSmall()
while x < 450 and y < 450:
    # Configurer la vitesse + le police et la position initiale de la tortue +
    # lever er descendre le stylo et dépalcer la tortue si besoin 
    turtle.pensize(1)
    turtle.speed(0)
    # print("goto while / " * 5)
    turtle.goto(x,y)
    # définir la position initiale de chaque petit carré 
    turtle.pendown()
    # Une fois la tortue à la positin initiale, redescendre le stylo pour commencer
    # print("X + 50 / " * 5)
    box(50)
    #carresid.append(i)
    #print(carresid)
    x = x + 50
    # Incrémenter le "x" de 50 afin de passer au prochain carré
    if x >= 50*9:
        x = 0
        y += 50
        # print('if' *20)
        turtle.penup()
        # lever le stylo afin de déplacer la tortue à la ligne 157 sans avoir laissé de trace
        turtle.goto(x,y)





turtle.done()
#turtle.bye()
