#Import des librairies/modules necessaire a mon programme
#A NE LANCER QU'UNE SEULE FOIS AU DEBUT
from pypot.creatures import PoppyErgoJr
import sys
import time


#Creation de l'objet python pour manipuler le robot
poppy = PoppyErgoJr()



#Affichage de la position actuelle de touts les moteurs

print(str(poppy.m1.present_position)+","+str(poppy.m2.present_position)+","+str(poppy.m3.present_position)+","+str(poppy.m4.present_position)+","+str(poppy.m5.present_position)+","+str(poppy.m6.present_position))

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
def nouvellePosition(p1,p2,p3,p4,p5,p6,temps):
    new_pos = {'m1': p1, 'm2': p2, 'm3': p3, 'm4': p4, 'm5': p5, 'm6': p6}
    poppy.goto_position(new_pos,temps,wait = True)
    
    
#Prends un pion en choisissant la hauteur (5: le pion le plus haut, 1: le pion le plus bas)
def prendsPion(h):
    activeTousLesMoteurs()
    #Leve toi
    print("Position veticale")
    nouvellePosition(-72.29,-6.3,7.48,0.44,89.88,20,1) 
    if (h == 5):
        print("Deplacement vers le haut de la pile")
        nouvellePosition(-69.35,-5.43,13.64,-1.32,-71.11,15.4,2) 
  

#serrage de la pince
def serrePion():
    poppy.m6.goto_position(0,0.5,wait = True)
    nouvellePosition(-72.29,-6.3,7.48,0.44,89.88,0,1) 
    
# deserrage de la pince
def deserrePion():
    poppy.m6.goto_position(24,1,wait = True)


#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------



#Code principal
prendsPion(5)
print("Serre Pion")
serrePion()
print("Leve le pion")

nouvellePosition(-111.29,-48.83,48.83,-22.43,20.67,-14.52,1) 
print("Dessere le pion")

deserrePion()
print("Attends 2 secondes")
time.sleep(2)
print("Repos")
ausecours()