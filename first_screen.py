import pygame


class Initial_Screen:
    def __init__(self, screen):
        self.font = pygame.font.Font(None, 60)
        self.small_font = pygame.font.Font(None, 30)
       # self.input_box = pygame.Rect(125, 300, 200, 30)
        self.input_box_surf = pygame.Surface((200, 30))
        self.input_box_rect = self.input_box_surf.get_rect(center = (225, 350))
        self.name = ""
        self.screen = screen
        
    def draw_text(self, text, position, screen, color="white"):
        text_surface = self.small_font.render(text, True, color)
        pygame.draw.rect(screen, "grey", self.input_box_rect, border_radius=25)    
        screen.blit(text_surface, position)

    def player_input(self, event_unicode):
        self.name += event_unicode
        self.draw_text(self.name, (135, 340), self.screen)

    def update(self, event):
        self.player_input(event)