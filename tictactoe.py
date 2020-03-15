#Import des librairies/modules necessaire a mon programme
#A NE LANCER QU'UNE SEULE FOIS AU DEBUT
from pypot.creatures import PoppyErgoJr
import sys
import time


#Creation de l'objet python pour manipuler le robot
poppy = PoppyErgoJr()

#AU SECOURS MET LES MOTEURS AU REPOS

def ausecours():
    #Active les moteurs
    for m in poppy.motors:
        m.compliant = False


    #reglage de la vitesse des moteurs
    for m in poppy.motors:
        m.moving_speed = 100

    poppy.m1.goal_position = 15.98
    poppy.m2.goal_position = 8.65
    poppy.m3.goal_position = 33.87
    poppy.m4.goal_position = 1.91
    poppy.m5.goal_position = 35.34
    poppy.m6.goal_position = -13.64    


    #On attend 5 secondes avant de desactiver
    time.sleep(5)

    #Deplacement des moteurs a la $position de repos
    poppy.m1.goal_position = -1.32
    poppy.m2.goal_position = -85.78
    poppy.m3.goal_position = -6.89
    poppy.m4.goal_position = 1.03
    poppy.m5.goal_position = 101.32
    poppy.m6.goal_position = -14.81


    #On attend 5 secondes avant de desactiver
    time.sleep(5)

    #Desactive les moteurs
    for m in poppy.motors:
        m.compliant = True

#DEFINITION DES FONCTIONS

def activeTousLesMoteurs():
    for m in poppy.motors:
        m.compliant = False

def desactiveTousLesMoteurs():
    for m in poppy.motors:
        m.compliant = True
    
#Fonction pour deplacer les moteurs a la position voulue
def nouvellePosition(p1,p2,p3,p4,p5,p6,v):
    poppy.m1.moving_speed = v
    poppy.m1.goal_position = p1
    poppy.m2.moving_speed = v
    poppy.m2.goal_position = p2
    poppy.m3.moving_speed = v
    poppy.m3.goal_position = p3
    poppy.m4.moving_speed = v
    poppy.m4.goal_position = p4
    poppy.m5.moving_speed = v
    poppy.m5.goal_position = p5
    poppy.m6.moving_speed = v
    poppy.m6.goal_position = p6

#Prends un pion en choisissant la hauteur (5: le pion le plus haut, 1: le pion le plus bas)
def prendsPion(h):
    activeTousLesMoteurs()
    if (h == 5):
        nouvellePosition(-45.89,-6.89,8.36,-21.26,-70.82,26.25,60) 
        time.sleep(5)

#serrage de la pince
def serrePion():
    poppy.m6.moving_speed = 80
    poppy.m6.goal_position = 7.5
    
# deserrage de la pince
def deserrePion():
    poppy.m6.moving_speed = 80
    poppy.m6.goal_position = 24



#Code principal
prendsPion(5)
serrePion()
time.sleep(2)
nouvellePosition(-111.29,-48.83,48.83,-22.43,20.67,-14.52,60) 
time.sleep(2)
deserrePion()
time.sleep(2)
ausecours()
