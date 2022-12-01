class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        '''
        Constructeur de la classe Button\n
        Paramètres:\n
                    - image
                    - pos (Tuple de 2) : Coordonné x et y du boutton
                    - texte_input (str) :
                    - font (Font) : 
                    - base_color :
                    - hovering_color :
        '''
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen) -> None:
        '''
        Mise à jour du bouton\n
        Paramètres:\n
                    - screen (Surface) : Surface de l écran
        '''
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position) -> bool:
        '''
        Vérifie si un bouton est présent à une position donnée\n
        Paramètres:\n
                    - position (Tuple de 2) : Position du bouton à vérifier
        '''
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position) -> None:
        '''
        Changer la couleur du bouton\n
        Paramètres:\n
                    position (Tuple de 2) : Position du bouton 
        '''
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)