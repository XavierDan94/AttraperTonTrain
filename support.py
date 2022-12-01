from os import walk
import pygame

def import_folder(path) -> list:
    '''
    Importer des fichiers (images)\n
    Paramètres:\n 
                - path (str) : Chemin relatif du fichier
    Retourne:\n
                - surfaces (list) : Liste des images
    '''
    surfaces = []

    # for folder_name, sub_folder, img_files
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surfaces.append(image_surf)

    return surfaces