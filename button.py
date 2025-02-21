import pygame

class Button():
    def __init__(self,image, position):
        self.image = pygame.image.load(image).convert_alpha()

        new_width = int(self.image.get_width() * 0.25)
        new_height = int(self.image.get_height() * 0.25)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))

        self.rect = self.image.get_rect(topleft = position)
        self.pressed = False

    def draw(self, window):
        window.blit(self.image, self.rect)

    def changePos(self, newPos):
        self.rect.topleft = newPos

    #make the button itself function lols
    def is_pressed(self, event):
        m_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(m_pos) and event.type == pygame.MOUSEBUTTONUP
        

    