import pygame
from classes.railway import *
class Train:
    def __init__(self, modele, capacite, numeroTrain, heureDepart) -> None:
        """
        Constructeur de la classe Train\n
        Paramètres:\n
                    - modele (str) : Modèle du train (TER ou TGV)
                    - capacite (int) : Capacité du train
                    - numeroTrain (int) : Numéro référence du train
                    - heureDepart (int) : Heure de départ du train (en secondes)
        """
        self.modele = modele
        self.capacite = capacite
        self.numero_train = numeroTrain    
        self.heure_depart = heureDepart

    def getHeureDepart(self) -> int:
        '''
        Accesseur de l heure de départ du train\n
        '''
        return self.heure_depart

    def setHeureDepart(self, newHeureDepart) -> None:
        '''
        Modificateur de l heure de départ\n
        Paramètres:\n
                    - newHeureDepart (int) : Nouvelle heure de départ en secondes
        '''
        self.heure_depart = newHeureDepart
