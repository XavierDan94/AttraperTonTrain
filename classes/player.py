import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos, group, collisionBoxes, railways, level) -> None:
        '''
        Constructeur de la classe Player\n
        Paramètres:\n
                    - pos (Tuple de 2): Positionnement du joueur
                    - group (list): Tableau contenant tout les sprites
                    - collisionBoxes (list(box)): Tableau des préparateurs de trains sur les voies nécessaire pour la détection de collision
                    - railways (list(Railway)): Tableau des voies
                    - level (Level) : Niveau du jeu en cours
        '''
        super().__init__(group)

        self.import_assets()
        self.status = 'down'
        self.frame_index = 0
                
        # general setup
        self.image = self.animations[self.status][self.frame_index]        
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['main']

        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 600

        # overlay 
        self.money = 500

        # collisions
        self.hitbox = self.rect.copy().inflate((-50,-100))
        self.collision_boxes = collisionBoxes
        self.all_sprites = group
        self.railways = railways
        self.level = level


    def import_assets(self) -> None:
        '''
        Importation des assets du joueur (graphics)\n
        '''
        self.animations = {'up': [],'down': [],'left': [],'right': [],
                           'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
                           'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
                           'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
                           'right_water':[],'left_water':[],'up_water':[],'down_water':[]}

        for animation in self.animations.keys():
            full_path = 'graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)


    def animate(self,dt):
        '''
        Animation du joueur\n
        Paramètres:\n
                    - dt : Nombre frames à afficher
        '''
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self) -> None:
        '''
        Détection des touches directionnels appuyées par le joueur\n
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'

        else:
            self.direction.x = 0

    def get_status(self) -> None:
        '''
        Récupère le status du joueur, pour savoir s'il est immobile ou non
        '''
        # Si le joueur ne bouge pas
        if self.direction.magnitude() == 0: 
            # on ajoute _idle au status
            self.status = self.status.split('_')[0] + '_idle'

    def move(self,dt) -> None:
        '''
        Déplacement du joueur\n
        Paramètres:\n
                    dt (float) : Frame à afficher
        '''
        # normalizing a vector 
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        new_pos_x = self.pos.x + self.direction.x * self.speed * dt
        if new_pos_x > 20 and new_pos_x < 800:
            self.pos.x += self.direction.x * self.speed * dt
            self.hitbox.centerx = round(self.pos.x)
            self.rect.centerx = self.hitbox.centerx
            self.detect_collision_boxes('horizontal')

        # vertical movement
        new_pos_y = self.pos.y + self.direction.y * self.speed * dt
        if new_pos_y > 120 and new_pos_y < 3500:
            self.pos.y += self.direction.y * self.speed * dt
            self.hitbox.centery = round(self.pos.y)
            self.rect.centery = self.hitbox.centery
            self.detect_collision_boxes('vertical')
        
    def detect_collision_boxes(self, direction) -> None:
        '''
        Détection de collision entre le joueur et les préparateurs de train des voies\n
        Paramètres:\n
                    - direction (str) : Axe de direction du joueur (horizontal ou vertical)
        '''
        for box in self.collision_boxes.sprites():
            if hasattr(box, 'hitbox'):
                if box.hitbox.colliderect(self.hitbox):
                    if direction == 'horizontal':
                        if self.direction.x > 0: # moving right
                            self.hitbox.right = box.hitbox.left
                        if self.direction.x < 0: # moving left
                            self.hitbox.left = box.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx

                    if direction == 'vertical':
                        if self.direction.y > 0: # moving down
                            self.hitbox.bottom = box.hitbox.top
                        if self.direction.y < 0: # moving up
                            self.hitbox.top = box.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery

                    railway_index = box.railway_number-1
                    self.level.preparation_train(railway_index)
                    

    def update(self,dt) -> None:
        '''
        Mise à jour du joueur\n
        Pramètres:\n
                    - dt (float) : Frames à afficher
        '''
        self.input()
        self.get_status()

        self.move(dt)
        self.animate(dt)
