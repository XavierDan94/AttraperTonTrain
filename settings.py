from pygame.math import Vector2
# screen
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
TILE_SIZE = 64

# overlay positions 
OVERLAY_POSITIONS = {
	'money' : (40, SCREEN_HEIGHT - 15), 
}

# overlay caracteristics
OVERLAY = {
	'background_color': (50, 57, 115)
}

# layers
LAYERS = {
	'ground': 1,
	'main': 2,
}

# Temps du niveau exprimé en secondes
TIME_LEVEL = 60*2

# Temps de spawn d'un train aléatoire en secondes
TIME_SPAWNED_TRAIN = 3.0

# Temps de départ d'un train dès qu'il est ajouté
TIME_DROPED_TRAIN = 10.0

# Temps requis pour préparer un train 
TIME_PREPARE_TRAIN = 1.0

# Temps de génération d'un événement alétoire permettant de générer un retard sur un train (en secondes)
TIME_EVENT = 15.0

# Score réglementation des points accordés
POINTS_BY_EACH_TRAIN_GONE_PREPARED = 50
POINTS_BY_EACH_TRAIN_GONE_NOT_PREPARED = -50