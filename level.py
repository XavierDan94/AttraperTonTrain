import pygame
from settings import *
from classes.player import Player
from classes.overlay import Overlay
from classes.sprites import Generic, Generic_Railway, Generic_Train, Generic_Box
from classes.railway import *
from support import *
from classes.tgv import * 
from classes.ter import *
import random

class Level:
    def __init__(self) -> None:
        '''
        Constructeur de la classe Level
        '''
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite groups
        self.all_sprites = CameraGroup()

        # score
        self.score = 0

        # temps et overlay
        self.clock = pygame.time.Clock()
        self.overlay = Overlay(self.score)

        # touche espace
        self.start_pressed_space = 0
        self.already_pressed_space = False
        self.time_pressed_space = 0

        # initialisation du niveau
        self.setup()

    def setup(self) -> None:
        '''
        Initialisateur du niveau
        '''
        # railways et trains (voies et trains)
        self.railways = []
        self.trains = []

        # boxes pour préparer le train 
        self.boxes = pygame.sprite.Group()

        # definition des voies et du tableau des heures de départ des trains
        for i in range (0,10):
            if i == 0:
                recty = 220
            else:
                recty = (220 + (i * 300))
            self.railways.append(Railway(i+1, None, recty))
            self.trains.append(-1)

        # Ajouts des voies et des trains dans les sprites (self.all_sprites) 
        for railway in self.railways:
            Generic_Railway((railway.rectX, railway.rectY), railway.background, self.all_sprites, "name")
            railway.computer = Generic_Box((railway.rectX, railway.rectY), railway.computer, self.all_sprites, railway.railway_number)
            self.boxes.add(railway.computer)
            if railway.train: 
                railway.train = Generic_Train((railway.rectX, railway.rectY), railway.train.background, self.all_sprites)
                
        # Ajout du joueur (Player) et du sol 
        self.player = Player((400,360), self.all_sprites, self.boxes, self.railways, self)
        Generic(
            pos = (0,0),
            surf = pygame.transform.scale(pygame.image.load('graphics/platform/main-platform.png'), (4000,4000)).convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['ground'])
        
    def run(self,dt) -> None:
        '''
        Lancement du niveau de jeu\n
        Paramètres:\n
                    - float (int) : Nombre d'image à afficher
        '''
        # level background
        self.display_surface.fill('black')
        
        # sprites draw and update
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)

        # Timer du spawn selon temps défini dans settings
        dt = self.clock.tick() / 1000
        if self.overlay.timer.getTotalSeconds() % TIME_SPAWNED_TRAIN == 0:
            self.addTrain()
        
        if self.overlay.timer.getTotalSeconds() in self.trains:
                index = self.trains.index(self.overlay.timer.getTotalSeconds())
                self.removeTrain(index)
        self.overlay.score = self.score
        self.overlay.display()

    def addTrain(self) -> None:
        '''
        Ajout aléatoire d'un train sur une voie qui n'en contient pas 
        '''
        railways_without_trains = [] # Initialisation du tableau contenant les voies sans train

        # On cherche les voies qui n'ont pas de train pour les ajouter au tableau railways_without_trains
        for railway in self.railways:
            if railway.hasTrain() == False:
                railways_without_trains.append(railway)

        # Uniquement s'il y a au moins une voie sans train
        if len(railways_without_trains) > 0:
            time = random.choice([TIME_DROPED_TRAIN])

            railway_choice = random.choice(railways_without_trains)

            if railway_choice.getRailwayNumber() != 1:
                train = TGV(400, 1000, self.overlay.timer.getTotalSeconds() + time)
            else:
                train = TER(200,1000, self.overlay.timer.getTotalSeconds() + time)

            railway_choice.addTrain(Generic_Train((railway_choice.rectX, railway_choice.rectY), train.getBackground(), self.all_sprites, train.getHeureDepart()))
            self.trains[self.railways.index(railway_choice)] = train.getHeureDepart()
            self.all_sprites.remove(railway_choice.computer)
            railway_choice.changeComputerWhenTrain()
            Generic_Box((railway_choice.rectX, railway_choice.rectY), railway_choice.computer, self.all_sprites, railway_choice.railway_number)
    
    def removeTrain(self, indexRailway) -> None:
            '''
            Suppression automatique d'un train\n
            Paramètres :\n
                        - indexRailway (int) : Position de la voie dans la liste des voies
            '''
            railway = self.railways[indexRailway]
            # Suppression du train dans le tableau des sprites (all_sprites), et dans le tableau des voies (railways)
            self.all_sprites.remove(railway.train)
            railway.removeTrain()
            # Suppression de l'ordinateur pour préparer le train dans le tableau des sprites (all_sprites)
            self.all_sprites.remove(railway.computer)
            railway.changeComputerWhenTrain()
            # Ajout du nouveau ordinateur pour préparer le train dans le tableau des sprites pour qu'il est la bonne couleur de bordure
            Generic_Box((railway.rectX, railway.rectY), railway.computer, self.all_sprites, railway.railway_number)
            # On supprime le train dans le tableau des trains (trains)
            self.trains[indexRailway] = -1
            # Mise à jour du score
            self.updateScore(railway)
   
    def preparation_train(self, railwayIndex) -> None:
        '''
        Préparation du train (en cours)\n
        Paramètres:\n
                        - railwayIndex : Positionnement dans la voie du tableau des voies (railways)
        '''
        railway = self.railways[railwayIndex] # Railway concerné
        keys = pygame.key.get_pressed()

        if railway.hasTrain() and railway.getTrainIsPrepared() == False:
            if keys[pygame.K_SPACE]:
                railway.prepareTrain()
                if self.already_pressed_space == False:
                    self.already_pressed_space = True
                    self.start_pressed_space = self.overlay.timer.getTotalSeconds()
                    self.time_pressed_space = 0 # Réinitialisation du temps maintenu de la touche espace

                self.time_pressed_space = self.overlay.timer.getTotalSeconds() - self.start_pressed_space
                if self.already_pressed_space and self.time_pressed_space >= TIME_PREPARE_TRAIN:
                    self.time_pressed_space = 0 # Réinitialisation du temps maintenu de la touche espace
                    self.configurer_train(railway)
               
    def configurer_train(self, railway) -> None:
        '''
        Configuration du train\n
        Paramètres:\n
                    - railway (int) : Voie qui est présent dans le tableau des voies (railways) -- voie concerné par la configuration du train
        '''

        if railway.hasTrain():
                self.all_sprites.remove(railway.computer)
                railway.changeComputerWhenTrainPrepared()
                Generic_Box((railway.rectX, railway.rectY), railway.computer, self.all_sprites, railway.railway_number)
                railway.train_is_prepared = True
                self.time_pressed_space = 0 # Réinitialisation du temps maintenu de la touche espace
                self.already_pressed_space = False

    def updateScore(self, railway) -> None:
        '''
        Mise à jour du score\n
        Paramètres:\n
                    - railway (Railway/Generic_Railway)
        '''
        # Le cas où le train a été préparer
        if railway.getTrainIsPrepared() == True:
            self.score += POINTS_BY_EACH_TRAIN_GONE_PREPARED
            railway.train_is_prepared = False

        # Si le cas n'a pas été préparer et que le score est strictement supérieur à 0
        elif self.score > 0 and railway.getTrainIsPrepared() == False:
            self.score += POINTS_BY_EACH_TRAIN_GONE_NOT_PREPARED


class CameraGroup(pygame.sprite.Group):
    
    def __init__(self) -> None:
        '''
        Constructeur de la classe CameraGroup\n
        '''
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player) -> None:
        '''
        Affichage personnalisée du joueur pour que la caméra le suit\n
        Paramètres :\n
                    - player (Player) : Joueur
        '''

        # Empêche le joueur de se déplacer dans une direction d'un axe selon une position x ou y donnée
        if player.rect.centerx - SCREEN_WIDTH / 2 > 800:
            self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        if player.rect.centery - SCREEN_HEIGHT / 2 > 0 and player.rect.centery <= 2000:
            self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

            
        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
                elif sprite.z == 6:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
